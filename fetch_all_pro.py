import os
import requests
import json
import time
from openai import OpenAI
from tqdm import tqdm
from dotenv import load_dotenv

# 1. 加载环境变量
load_dotenv()

print(f"--- 环境检查 ---")
print(f"Debug - Session: {os.getenv('LEETCODE_SESSION')[:15] if os.getenv('LEETCODE_SESSION') else 'None'}...")
print(f"Debug - CSRF: {os.getenv('LEETCODE_CSRFTOKEN')}")
print(f"Debug - OpenAI Key: {'已找到' if os.getenv('CHATGPT_TOKEN') else '未找到'}")
print(f"----------------\n")

# ================= 配置区 =================
client = OpenAI(api_key=os.getenv('CHATGPT_TOKEN'))
LC_SESSION = os.getenv('LEETCODE_SESSION')
LC_CSRF = os.getenv('LEETCODE_CSRFTOKEN')

TEST_MODE = False  # 测试模式
TEST_LIMIT = 10

HEADERS = {
    'Cookie': f'LEETCODE_SESSION={LC_SESSION}; csrftoken={LC_CSRF}',
    'x-csrftoken': LC_CSRF,
    'Referer': 'https://leetcode.com',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}


# ================= 功能函数 =================

def get_ac_questions_list(limit=2000):
    """获取所有已通过题目的基础信息 (修复了 offset 参数错误)"""
    url = "https://leetcode.com/graphql"
    # 将之前的 offset 更改为 skip
    query = """
    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
      problemsetQuestionList: questionList(
        categorySlug: $categorySlug
        limit: $limit
        skip: $skip
        filters: $filters
      ) {
        questions: data {
          questionId
          titleSlug
        }
      }
    }
    """
    variables = {
        "categorySlug": "",
        "skip": 0,
        "limit": limit,
        "filters": {"status": "AC"}
    }
    try:
        resp = requests.post(url, json={'query': query, 'variables': variables}, headers=HEADERS)
        resp.raise_for_status()
        data = resp.json().get('data', {}).get('problemsetQuestionList', {}).get('questions', [])
        return data
    except Exception as e:
        print(f"❌ 获取题目列表失败: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"服务器详情: {e.response.text}")
        return []


def get_problem_metadata(slug):
    """获取题目标签、难度等元数据"""
    query = """
    query singleQuestion($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            topicTags { name translatedName }
            difficulty
        }
    }
    """
    try:
        resp = requests.post("https://leetcode.com/graphql",
                             json={'query': query, 'variables': {'titleSlug': slug}},
                             headers=HEADERS).json()
        q = resp.get('data', {}).get('question', {})
        tags = [t['translatedName'] or t['name'] for t in q.get('topicTags', [])]
        return tags, q.get('difficulty', 'Unknown'), q.get('questionId')
    except:
        return [], "Unknown", None


def get_all_ac_submissions(slug):
    """获取 AC 提交记录列表"""
    query = """
    query submissionList($questionSlug: String!, $offset: Int, $limit: Int) {
        submissionList(questionSlug: $questionSlug, offset: $offset, limit: $limit) {
            submissions { id statusDisplay lang }
        }
    }
    """
    params = {'query': query, 'variables': {'offset': 0, 'limit': 10, 'questionSlug': slug}}
    try:
        resp = requests.post("https://leetcode.com/graphql", json=params, headers=HEADERS).json()
        subs = resp.get('data', {}).get('submissionList', {}).get('submissions', [])
        return [s for s in subs if s['statusDisplay'] == 'Accepted']
    except:
        return []


def get_submission_code(sub_id):
    """提取源代码"""
    query = """
    query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) { code }
    }
    """
    try:
        resp = requests.post("https://leetcode.com/graphql",
                             json={'query': query, 'variables': {'submissionId': int(sub_id)}},
                             headers=HEADERS).json()
        return resp.get('data', {}).get('submissionDetails', {}).get('code', "")
    except:
        return ""


def get_problem_cn(slug):
    """获取中文题目描述"""
    query = """
    query translatedConfig($titleSlug: String!) {
        question(titleSlug: $titleSlug) { translatedTitle translatedContent }
    }
    """
    try:
        resp = requests.post("https://leetcode.cn/graphql",
                             json={'query': query, 'variables': {'titleSlug': slug}}).json()
        return resp.get('data', {}).get('question')
    except:
        return None


def ai_analyze(title, code):
    """GPT-4o 深度复盘"""
    prompt = (
        f"请分析算法题《{title}》的实现逻辑。\n"
        f"要求：\n1. 一句话直击本质：用一句话总结该算法的核心逻辑。\n"
        f"2. 提供简洁的中文实现思路描述。\n"
        f"3. 总结AC版本所有的通用解决方式/逻辑的中文伪代码。\n"
        f"4. 使用 LaTeX 格式给出时间复杂度和空间复杂度，例如 $O(n)$。\n\n"
        f"代码如下：\n{code}"
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "你是一个严谨的算法专家。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI 复盘生成失败: {e}"


# ================= 主程序 =================

def main():
    print("🚀 开始运行 LeetCode 同步程序...")
    all_questions = get_ac_questions_list()

    if not all_questions:
        print("❌ 未获取到任何已通过题目，请检查 Session 和 CSRFToken。")
        return

    if TEST_MODE:
        print(f"🧪 测试模式开启：仅处理前 {TEST_LIMIT} 题")
        all_questions = all_questions[:TEST_LIMIT]

    print(f"🎯 待处理题目: {len(all_questions)} 题")

    if not os.path.exists("Problems"):
        os.makedirs("Problems")

    metadata_list = []
    for q_basic in tqdm(all_questions, desc="📦 处理中"):
        slug = q_basic['titleSlug']
        try:
            tags, difficulty, q_id = get_problem_metadata(slug)
            prob_cn = get_problem_cn(slug)
            title = (prob_cn['translatedTitle'] if prob_cn else slug) or slug

            folder_name = f"{q_id}_{slug}" if q_id else slug
            folder_path = f"Problems/{folder_name}"

            if os.path.exists(f"{folder_path}/README_CN.md") and not TEST_MODE:
                continue

            os.makedirs(folder_path, exist_ok=True)
            ac_subs = get_all_ac_submissions(slug)

            if ac_subs:
                latest_sub = ac_subs[0]
                code = get_submission_code(latest_sub['id'])
                ext = {"python": "py", "python3": "py", "java": "java", "cpp": "cpp"}.get(latest_sub['lang'], "txt")

                with open(f"{folder_path}/solution.{ext}", 'w', encoding='utf-8') as f:
                    f.write(code)

                analysis = ai_analyze(title, code)

                with open(f"{folder_path}/README_CN.md", 'w', encoding='utf-8') as f:
                    tag_str = " ".join([f"`{t}`" for t in tags])
                    f.write(f"# {q_id}. {title}\n\n")
                    f.write(f"**难度**: {difficulty} | **标签**: {tag_str}\n\n")
                    f.write(f"## 题目描述\n\n{prob_cn['translatedContent'] if prob_cn else '暂无描述'}\n\n---\n")
                    f.write(f"## 解题思路与复盘\n\n{analysis}")

            metadata_list.append({"id": q_id, "title": title, "slug": slug, "difficulty": difficulty})
            time.sleep(1)

        except Exception as e:
            print(f"\n❌ 处理题目 {slug} 时出错: {e}")
            continue

    with open("summary.json", "w", encoding="utf-8") as f:
        json.dump(metadata_list, f, ensure_ascii=False, indent=2)

    print("\n✅ 同步完成！")


if __name__ == "__main__":
    main()
