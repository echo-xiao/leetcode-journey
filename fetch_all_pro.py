import os
import requests
import json
import time
import anthropic
from tqdm import tqdm
from dotenv import load_dotenv

# 1. 初始化
load_dotenv()

# The analysis runs on Claude; the key lives in .env as CLAUDE_TOKEN.
CLAUDE_MODEL = "claude-sonnet-5"
claude = anthropic.Anthropic(api_key=os.getenv('CLAUDE_TOKEN'))

# --- 环境检查 ---
LC_SESSION = os.getenv('LEETCODE_SESSION')
LC_CSRF = os.getenv('LEETCODE_CSRFTOKEN')
CLAUDE_KEY = os.getenv('CLAUDE_TOKEN')

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
print(f"Debug - Claude Key: {'已找到' if CLAUDE_KEY else '未找到'}")
print(f"----------------\n")

# ================= 配置区 =================
TEST_MODE = False  # True: 只处理前 TEST_LIMIT 题，用于调试
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
        questionId difficulty content
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
        # 先尝试从中文站获取
        cn = \
        requests.post(f"{BASE_URL_CN}/graphql", json={'query': q_cn, 'variables': {'titleSlug': slug}}).json()['data'][
            'question']
        # 如果中文站没有返回描述，用英文站的 content 补充
        if not cn or not cn.get('translatedContent'):
            if cn is None:
                cn = {}
            cn['translatedContent'] = meta.get('content')
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


def read_existing_description(folder):
    """Recover a previously fetched problem statement.

    Current layout keeps it in problem.md; older folders kept it inside
    README_CN.md. Try both so a re-fetch never downgrades a good description
    to '暂无描述'.
    """
    import re as _re
    for name in ("problem.md", "README_CN.md"):
        path = f"{folder}/{name}"
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        m = _re.search(r'## 题目描述\n\n(.+?)(?:\n\n---|\Z)', content, _re.DOTALL)
        if m and m.group(1).strip() not in ('None', '暂无描述', ''):
            return m.group(1).strip()
    return None


def write_problem_files(folder, q_id, cn_title, difficulty, tags,
                        main_cat, sub_cat, description, analysis):
    """Write the four-file layout for one problem.

    README_CN.md  index (GitHub renders it when the folder is opened)
    problem.md    problem statement
    pseudocode.md approach, pseudocode and complexity
    elements.md   framework slots — only created as a placeholder here;
                  tools/build_elements.py fills in the per-problem answers.
    """
    title = f"{q_id}. {cn_title}"
    tag_str = " ".join([f"`{t}`" for t in tags])
    meta = f"**难度**: {difficulty} | **标签**: {tag_str}\n\n**归类**: {main_cat} > {sub_cat}"

    with open(f"{folder}/problem.md", 'w', encoding='utf-8') as f:
        f.write(f"# {title} · 题目\n\n{meta}\n\n## 题目描述\n\n{description}\n")

    with open(f"{folder}/pseudocode.md", 'w', encoding='utf-8') as f:
        f.write(f"# {title} · 解题思路与伪代码\n\n{analysis}\n")

    elements_path = f"{folder}/elements.md"
    if not os.path.exists(elements_path):
        with open(elements_path, 'w', encoding='utf-8') as f:
            f.write(f"# {title} · 要素\n\n还没生成，运行 tools/build_elements.py 补上。\n")

    with open(f"{folder}/README_CN.md", 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n{meta}\n\n")
        f.write("- [题目](problem.md)\n")
        f.write("- [解题思路与伪代码](pseudocode.md)\n")
        f.write("- [要素](elements.md)\n")


def ai_analyze_all_versions(title, codes_dict):
    """Summarise every AC version of one problem into the pseudocode section.

    Runs on Claude via the repo's CLAUDE_TOKEN. The four numbered parts are
    what pseudocode.md is built from, so the shape here is load-bearing.
    """
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
        message = claude.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=8000,
            thinking={"type": "adaptive"},
            output_config={"effort": "medium"},
            system="你是一个严谨的算法专家。",
            messages=[{"role": "user", "content": prompt}],
        )
        return "".join(b.text for b in message.content if b.type == "text")
    except Exception as e:
        return f"AI 复盘生成失败: {e}"


def classify_question(tags, title):
    """
    核心分类逻辑：基于 LeetCode 标签将题目映射至 12 大类体系
    """
    tag_set = {t.lower() for t in tags}

    # 映射配置：大类名称 -> 匹配的 LeetCode 英文标签或关键字
    mapping = {
        "1. 滑动窗口与双指针": ["sliding window", "two pointers", "双指针", "滑动窗口"],
        "2. 二分算法": ["binary search", "二分查找", "二分"],
        "3. 单调栈": ["monotonic stack", "单调栈", "单调队列"],
        "4. 网格图": ["matrix", "grid", "矩阵"],
        "5. 位运算": ["bit manipulation", "位运算"],
        "6. 图论算法": ["graph", "topological sort", "shortest path", "minimum spanning tree", "图", "拓扑排序"],
        "7. 动态规划": ["dynamic programming", "backpack", "memoization", "动态规划"],
        "8. 常用数据结构": ["stack", "queue", "heap", "priority queue", "trie", "union find", "fenwick tree",
                            "segment tree", "prefix sum", "hash table", "堆", "并查集", "前缀和"],
        "9. 数学算法": ["math", "number theory", "combinatorics", "geometry", "probability", "数学", "数论",
                        "组合数学"],
        "10. 贪心与思维": ["greedy", "brainteaser", "constructive", "贪心", "脑筋急转弯"],
        "11. 链表、树与回溯": ["linked list", "tree", "binary tree", "backtracking", "dfs", "bfs", "depth-first search",
                              "breadth-first search", "链表", "二叉树", "回溯"],
        "12. 字符串": ["string", "string matching", "kmp", "ac automaton", "字符串"]
    }

    for main_cat, keywords in mapping.items():
        if any(k in tag_set for k in keywords):
            # 取第一个原始标签作为小类，若无则设为 General
            sub_cat = tags[0] if tags else "General"
            return main_cat, sub_cat

    return "13. 其他", "未分类"


def main():
    print("🚀 开始运行 LeetCode 同步程序...")
    all_questions = get_all_ac_questions(session)

    if not all_questions:
        print("❌ 未获取到题目，请检查配置。")
        return

    if TEST_MODE:
        print(f"🧪 测试模式开启：仅处理前 {TEST_LIMIT} 题")
        all_questions = all_questions[:TEST_LIMIT]

    if not os.path.exists("Problems"):
        os.makedirs("Problems")

    # 用于生成 summary.json 的汇总列表
    summary_data = []

    for q_basic in tqdm(all_questions, desc="📦 深度同步中"):
        slug = q_basic['titleSlug']
        try:
            q_id, difficulty, tags, prob_cn = get_problem_details(slug)
            cn_title = (prob_cn['translatedTitle'] if prob_cn else slug) or slug
            folder = f"Problems/{q_id}_{slug}"

            # 1. 自动分类
            main_cat, sub_cat = classify_question(tags, cn_title)

            # 2. 收集 JSON 数据 (包含 6 个核心字段)
            summary_data.append({
                "id": q_id,
                "title_cn": cn_title,
                "title_en": slug,
                "difficulty": difficulty,
                "category_main": main_cat,
                "category_sub": sub_cat,
                "tags": tags
            })

            # 断点续传
            if os.path.exists(f"{folder}/README_CN.md") and not TEST_MODE:
                continue

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

                with open(f"{folder}/solution_{i + 1}.{ext}", 'w', encoding='utf-8') as f:
                    f.write(code)
                all_codes[f"{sub['id']}_{lang}"] = code

            # AI 综合分析
            analysis = ai_analyze_all_versions(cn_title, all_codes)

            # 3. 写入 Markdown，同时标注分类
            existing_desc = read_existing_description(folder)
            new_desc = prob_cn.get('translatedContent') if prob_cn and prob_cn.get('translatedContent') else None
            description = new_desc or existing_desc or '暂无描述'

            write_problem_files(folder, q_id, cn_title, difficulty, tags,
                                main_cat, sub_cat, description, analysis)

            time.sleep(0.5)

        except Exception as e:
            print(f"\n❌ 处理 {slug} 出错: {e}")
            continue

    # 4. 持久化 summary.json
    with open("summary.json", "w", encoding="utf-8") as f:
        json.dump(summary_data, f, ensure_ascii=False, indent=4)

    print(f"\n✅ 同步完成！summary.json 已更新，共计 {len(summary_data)} 题。")





if __name__ == "__main__":
    main()



