import os
import requests
import json
import time
import anthropic
from dotenv import load_dotenv

# 1. Initialization
load_dotenv()

# The analysis runs on Claude; the key lives in .env as CLAUDE_TOKEN.
CLAUDE_MODEL = "claude-sonnet-5"
claude = anthropic.Anthropic(api_key=os.getenv('CLAUDE_TOKEN'))

# --- Environment check ---
LC_SESSION = os.getenv('LEETCODE_SESSION')
LC_CSRF = os.getenv('LEETCODE_CSRFTOKEN')
CLAUDE_KEY = os.getenv('CLAUDE_TOKEN')

# ================= Core: authenticated session setup =================
# A global Session object that manages cookies and headers automatically
session = requests.Session()

# Inject the identity cookies (the key to fixing the "0 problems" issue)
session.cookies.set('LEETCODE_SESSION', LC_SESSION, domain='leetcode.com')
session.cookies.set('csrftoken', LC_CSRF, domain='leetcode.com')

# Shared default headers
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Referer': 'https://leetcode.com',
    'x-csrftoken': LC_CSRF,
    'Content-Type': 'application/json'
})


def describe_environment() -> str:
    """What the module found in .env, for callers that want to log it.

    Printing this at import time made the module unusable as a library: every
    command that touched it dumped four lines of diagnostics first.
    """
    return (
        f"Session: {'set' if LC_SESSION else 'missing'} | "
        f"CSRF: {'set' if LC_CSRF else 'missing'} | "
        f"Claude Key: {'set' if CLAUDE_KEY else 'missing'}"
    )


# ================= Configuration =================
BASE_URL_EN = "https://leetcode.com"
BASE_URL_CN = "https://leetcode.cn"


# ================= API functions (all going through the session) =================

def get_total_ac_count():
    """The user's true total of accepted problems."""
    # api/problems/all/ exposes num_solved directly, which is the simplest way
    url = f"{BASE_URL_EN}/api/problems/all/"
    try:
        resp = session.get(url)  # request through the authenticated session
        data = resp.json()
        # Print the username too, to confirm we're logged in as the right user
        print(f"👤 Logged in as: {data.get('user_name', 'unknown')}")
        return data.get('num_solved', 0)
    except Exception as e:
        print(f"Failed to fetch total: {e}")
        return 0


def get_all_ac_questions(session):
    """
    Fetch the slugs of all accepted problems, page by page.
    """
    total = get_total_ac_count()
    print(f"📊 Total accepted problems on the account: {total}")

    questions = []
    page_size = 100

    # 1. Updated query with the $categorySlug parameter added
    query = """
    query problemsetQuestionList($limit: Int, $skip: Int, $filters: QuestionListFilterInput, $categorySlug: String) {
      problemsetQuestionList: questionList(limit: $limit, skip: $skip, filters: $filters, categorySlug: $categorySlug) {
        questions: data { questionId titleSlug }
      }
    }
    """

    for skip in range(0, total, page_size):
        # 2. Add categorySlug to vars; the empty string "" means all categories
        vars = {
            "limit": page_size,
            "skip": skip,
            "filters": {"status": "AC"},
            "categorySlug": ""  # the empty string here is what makes this work
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
                print(f"✅ Fetched {len(questions)} / {total}")
            else:
                print(f"⚠️ Unexpected response: {data}")
                break

            time.sleep(0.8)
        except Exception as e:
            print(f"❌ Request failed: {e}")
            break

    return questions



def get_recent_ac_submissions(username, limit=20):
    """The most recent accepted submissions, newest first.

    Public: no cookie needed, the same way the profile calendar is. LeetCode
    caps the response at twenty however large `limit` is, which is why this
    refreshes recent activity rather than replacing the backfill.
    """
    query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
      recentAcSubmissionList(username: $username, limit: $limit) {
        id title titleSlug timestamp
      }
    }
    """
    resp = requests.post(
        f"{BASE_URL_EN}/graphql",
        json={"query": query, "variables": {"username": username, "limit": limit}},
        headers={"Content-Type": "application/json", "Referer": BASE_URL_EN,
                 "User-Agent": session.headers["User-Agent"]},
        timeout=15,
    )
    data = resp.json()
    return (data.get("data") or {}).get("recentAcSubmissionList") or []


def get_problem_details(slug):
    """Fetch metadata and the Chinese statement across both sites."""
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
        # Try the Chinese site first
        cn = \
        requests.post(f"{BASE_URL_CN}/graphql", json={'query': q_cn, 'variables': {'titleSlug': slug}}).json()['data'][
            'question']
        # If the Chinese site returned no statement, fall back to the English content
        if not cn or not cn.get('translatedContent'):
            if cn is None:
                cn = {}
            cn['translatedContent'] = meta.get('content')
        tags = [t['translatedName'] or t['name'] for t in meta.get('topicTags', [])]
        return meta['questionId'], meta['difficulty'], tags, cn
    except:
        return None, "Unknown", [], None


def get_all_ac_submissions(slug):
    """All accepted submissions for one problem."""
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
    """The source code of one submission."""
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
        return f"AI analysis failed: {e}"


def classify_question(tags, title):
    """
    Core classification: map a problem into the 12-category system by its LeetCode tags.

    The Chinese category names below are data, not UI — they are written into
    Notion and README_CN.md and must stay byte-identical to existing rows.
    """
    tag_set = {t.lower() for t in tags}

    # Mapping: category name -> matching LeetCode tags/keywords (English and Chinese)
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
            # Use the first raw tag as the subcategory, or General if there is none
            sub_cat = tags[0] if tags else "General"
            return main_cat, sub_cat

    return "13. 其他", "未分类"
