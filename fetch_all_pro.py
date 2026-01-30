import os
import requests
import json
import time
from openai import OpenAI
from tqdm import tqdm
from dotenv import load_dotenv

# 1. 初始化
load_dotenv()
client = OpenAI(api_key=os.getenv('CHATGPT_TOKEN'))

# --- 环境检查 ---
LC_SESSION = os.getenv('LEETCODE_SESSION')
LC_CSRF = os.getenv('LEETCODE_CSRFTOKEN')
OPENAI_KEY = os.getenv('CHATGPT_TOKEN')

# ================= 核心：身份验证 Session 配置 =================
# 创建一个全局 Session 对象，它会自动管理 Cookie 和 Header
session = requests.Session()

# 注入身份 Cookie（解决 0 题问题的关键）
session.cookies.set('LEETCODE_SESSION', LC_SESSION, domain='leetcode.com')
session.cookies.set('csrftoken', LC_CSRF, domain='leetcode.com')

# 设置全局通用的 Header
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Referer': 'https://leetcode.com',
    'x-csrftoken': LC_CSRF,
    'Content-Type': 'application/json'
})

print(f"--- 环境检查 ---")
print(f"Debug - Session: {LC_SESSION[:15] if LC_SESSION else 'None'}...")
print(f"Debug - CSRF: {LC_CSRF[:15] if LC_CSRF else 'None'}...")
print(f"Debug - OpenAI Key: {'已找到' if OPENAI_KEY else '未找到'}")
print(f"----------------\n")

# ================= 配置区 =================
TEST_MODE = False  # ⭐ True: 仅测试 10 题; False: 全量同步 364+ 题
TEST_LIMIT = 10
BASE_URL_EN = "https://leetcode.com"
BASE_URL_CN = "https://leetcode.cn"


# ================= 功能函数（已切换至 session） =================

def get_total_ac_count():
    """获取用户 AC 题目的真实总数"""
    # 也可以直接访问 api/problems/all/ 获取 num_solved，更直接
    url = f"{BASE_URL_EN}/api/problems/all/"
    try:
        resp = session.get(url)  # 使用 session 发起请求
        data = resp.json()
        # 顺便打印一下当前用户名，确认没走错房间
        print(f"👤 当前登录用户: {data.get('user_name', '未知')}")
        return data.get('num_solved', 0)
    except Exception as e:
        print(f"获取总数失败: {e}")
        return 0


def get_all_ac_questions(session):
    """
    分页获取所有通过题目的 Slug
    """
    total = get_total_ac_count()
    print(f"📊 账户内已通过题目总数: {total}")

    questions = []
    page_size = 100

    # 1. 更新后的查询语句，加入了 $categorySlug 参数
    query = """
    query problemsetQuestionList($limit: Int, $skip: Int, $filters: QuestionListFilterInput, $categorySlug: String) {
      problemsetQuestionList: questionList(limit: $limit, skip: $skip, filters: $filters, categorySlug: $categorySlug) {
        questions: data { questionId titleSlug }
      }
    }
    """

    for skip in range(0, total, page_size):
        # 2. 在 vars 中增加 categorySlug，传空字符串 "" 代表获取所有分类
        vars = {
            "limit": page_size,
            "skip": skip,
            "filters": {"status": "AC"},
            "categorySlug": ""  # 这里的空字符串是解决问题的关键
        }

        try:
            resp = session.post(
                f"{BASE_URL_EN}/graphql",
                json={'query': query, 'variables': vars},
                timeout=10
            )

            data = resp.json()
            if 'data' in data and data['data']['problemsetQuestionList']:
                questions.extend(data['data']['problemsetQuestionList']['questions'])
                print(f"✅ 已抓取 {len(questions)} / {total}")
            else:
                print(f"⚠️ 响应异常: {data}")
                break

            time.sleep(0.8)
        except Exception as e:
            print(f"❌ 请求出错: {e}")
            break

    return questions



def get_problem_details(slug):
    """跨站获取元数据与中文内容"""
    q_meta = """
    query singleQuestion($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId difficulty
        topicTags { name translatedName }
      }
    }
    """
    q_cn = """
    query translatedConfig($titleSlug: String!) {
      question(titleSlug: $titleSlug) { translatedTitle translatedContent }
    }
    """
    try:
        meta = \
        session.post(f"{BASE_URL_EN}/graphql", json={'query': q_meta, 'variables': {'titleSlug': slug}}).json()['data'][
            'question']
        # 中文站不需要身份验证，直接请求
        cn = \
        requests.post(f"{BASE_URL_CN}/graphql", json={'query': q_cn, 'variables': {'titleSlug': slug}}).json()['data'][
            'question']
        tags = [t['translatedName'] or t['name'] for t in meta.get('topicTags', [])]
        return meta['questionId'], meta['difficulty'], tags, cn
    except:
        return None, "Unknown", [], None


def get_all_ac_submissions(slug):
    """获取该题目下所有 AC 提交记录"""
    all_ac_subs = []
    offset, limit = 0, 20
    query = """
    query submissionList($questionSlug: String!, $offset: Int, $limit: Int) {
        submissionList(questionSlug: $questionSlug, offset: $offset, limit: $limit) {
            submissions { id statusDisplay lang timestamp }
        }
    }
    """
    while True:
        vars = {'offset': offset, 'limit': limit, 'questionSlug': slug}
        try:
            resp = session.post(f"{BASE_URL_EN}/graphql", json={'query': query, 'variables': vars}).json()
            subs = resp.get('data', {}).get('submissionList', {}).get('submissions', [])
            if not subs: break
            ac_in_page = [s for s in subs if s['statusDisplay'] == 'Accepted']
            all_ac_subs.extend(ac_in_page)
            offset += limit
            time.sleep(0.3)
        except:
            break
    return all_ac_subs


def get_submission_code(sub_id):
    """获取具体代码"""
    query = "query submissionDetails($submissionId: Int!) { submissionDetails(submissionId: $submissionId) { code } }"
    try:
        resp = session.post(f"{BASE_URL_EN}/graphql",
                            json={'query': query, 'variables': {'submissionId': int(sub_id)}}).json()
        return resp.get('data', {}).get('submissionDetails', {}).get('code', "")
    except:
        return ""


def ai_analyze_all_versions(title, codes_dict):
    """GPT-4o 综合分析所有 AC 版本"""
    code_context = ""
    for i, (key, code) in enumerate(codes_dict.items()):
        code_context += f"--- 版本 {i + 1} (ID: {key}) ---\n{code}\n\n"

    prompt = (
        f"请分析算法题《{title}》的所有 AC 版本实现逻辑。\n"
        f"要求：\n"
        f"1. 一句话直击本质：用一句话总结该算法的核心逻辑。\n"
        f"2. 综合思路：如果存在多种解法（如递归与迭代、DFS与BFS、不同数据结构），请分别简述。\n"
        f"3. 全量伪代码：总结所有 AC 版本中涉及的不同类型逻辑的中文伪代码。\n"
        f"4. 复杂度：使用 LaTeX 格式给出时间及空间复杂度，例如 $O(n)$。\n\n"
        f"代码集如下：\n{code_context}"
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "你是一个严谨的算法专家。"}, {"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI 复盘生成失败: {e}"



# ================= 主程序 =================

def main():
    print("🚀 开始运行 LeetCode 同步程序...")

    # --- 修改这里：传入上面定义好的 session ---
    all_questions = get_all_ac_questions(session)
    # ---------------------------------------

    if not all_questions:
        print("❌ 未获取到题目，请检查配置。")
        return

    if TEST_MODE:
        print(f"🧪 测试模式开启：仅处理前 {TEST_LIMIT} 题")
        all_questions = all_questions[:TEST_LIMIT]

    if not os.path.exists("Problems"): os.makedirs("Problems")

    for q_basic in tqdm(all_questions, desc="📦 深度同步中"):
        slug = q_basic['titleSlug']
        try:
            q_id, difficulty, tags, prob_cn = get_problem_details(slug)
            title = (prob_cn['translatedTitle'] if prob_cn else slug) or slug
            folder = f"Problems/{q_id}_{slug}"

            # 断点续传
            if os.path.exists(f"{folder}/README_CN.md") and not TEST_MODE: continue

            os.makedirs(folder, exist_ok=True)
            ac_subs = get_all_ac_submissions(slug)

            if not ac_subs: continue

            all_codes = {}
            for i, sub in enumerate(ac_subs):
                code = get_submission_code(sub['id'])
                if not code: continue

                lang = sub['lang']
                ext = {"python": "py", "python3": "py", "java": "java", "cpp": "cpp", "javascript": "js"}.get(lang,
                                                                                                              "txt")

                # 保存所有历史版本：solution_1.py, solution_2.py...
                with open(f"{folder}/solution_{i + 1}.{ext}", 'w', encoding='utf-8') as f:
                    f.write(code)

                all_codes[f"{sub['id']}_{lang}"] = code

            # AI 对所有版本进行综合复盘
            analysis = ai_analyze_all_versions(title, all_codes)

            with open(f"{folder}/README_CN.md", 'w', encoding='utf-8') as f:
                tag_str = " ".join([f"`{t}`" for t in tags])
                f.write(f"# {q_id}. {title}\n\n")
                f.write(f"**难度**: {difficulty} | **标签**: {tag_str}\n\n")
                f.write(f"## 题目描述\n\n{prob_cn['translatedContent'] if prob_cn else '暂无描述'}\n\n---\n")
                f.write(f"## 解题思路与复盘\n\n{analysis}")

            time.sleep(1)

        except Exception as e:
            print(f"\n❌ 处理 {slug} 出错: {e}")
            continue

    print("\n✅ 同步完成！已更新所有历史 AC 记录。")


if __name__ == "__main__":
    main()
