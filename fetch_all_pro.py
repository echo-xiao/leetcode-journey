import os
import requests
import json
import time
from openai import OpenAI
from tqdm import tqdm
from dotenv import load_dotenv

# 1. 初始化配置
load_dotenv()
LC_SESSION = os.getenv('LEETCODE_SESSION')
LC_CSRF = os.getenv('LEETCODE_CSRFTOKEN')
OPENAI_KEY = os.getenv('CHATGPT_TOKEN')

# 验证环境变量
print(f"--- 环境检查 ---")
print(f"Debug - Session: {LC_SESSION[:10] if LC_SESSION else 'None'}...")
print(f"Debug - OpenAI: {'Ready' if OPENAI_KEY else 'Missing'}")
print(f"----------------\n")

client = OpenAI(api_key=OPENAI_KEY)

# ================= 配置区 =================
# ⭐⭐⭐ 全量开关在这里 ⭐⭐⭐
TEST_MODE = True    # True: 只运行 10 题测试; False: 运行全量 364+ 题
TEST_LIMIT = 10     # 测试模式下的题目数量

BASE_URL_EN = "https://leetcode.com"
BASE_URL_CN = "https://leetcode.cn"

HEADERS = {
    'Cookie': f'LEETCODE_SESSION={LC_SESSION}; csrftoken={LC_CSRF}',
    'x-csrftoken': LC_CSRF,
    'Referer': BASE_URL_EN,
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

# ================= 核心逻辑：分页获取所有题目 =================

def get_total_ac_count():
    """获取用户 AC 题目的真实总数"""
    query = "query userStatus { userProgress { numAccepted { count } } }"
    try:
        resp = requests.post(f"{BASE_URL_EN}/graphql", json={'query': query}, headers=HEADERS)
        return resp.json()['data']['userProgress']['numAccepted'][0]['count']
    except: return 0

def get_all_ac_questions():
    """优雅进阶法：分页抓取所有题目索引"""
    total = get_total_ac_count()
    print(f"📊 检测到已通过题目总数: {total}")
    
    questions = []
    page_size = 100
    query = """
    query problemsetQuestionList($limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
      problemsetQuestionList: questionList(limit: $limit, skip: $skip, filters: $filters) {
        questions: data { questionId titleSlug }
      }
    }
    """
    for skip in range(0, total, page_size):
        vars = {"limit": page_size, "skip": skip, "filters": {"status": "AC"}}
        try:
            resp = requests.post(f"{BASE_URL_EN}/graphql", json={'query': query, 'variables': vars}, headers=HEADERS)
            questions.extend(resp.json()['data']['problemsetQuestionList']['questions'])
            time.sleep(0.5)
        except: break
    return questions

# ================= 核心逻辑：全量代码抓取 =================

def get_all_accepted_codes(slug):
    """抓取该题目下【所有】AC 提交记录的代码"""
    list_query = """
    query submissionList($questionSlug: String!, $offset: Int, $limit: Int) {
      submissionList(questionSlug: $questionSlug, offset: $offset, limit: $limit) {
        submissions { id statusDisplay lang timestamp }
      }
    }
    """
    detail_query = """
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) { code }
    }
    """
    all_ac_records = []
    try:
        resp = requests.post(f"{BASE_URL_EN}/graphql", 
                             json={'query': list_query, 'variables': {'questionSlug': slug, 'offset': 0, 'limit': 100}}, 
                             headers=HEADERS).json()
        subs = resp['data']['submissionList']['submissions']
        ac_subs = [s for s in subs if s['statusDisplay'] == 'Accepted']
        
        for sub in ac_subs:
            detail = requests.post(f"{BASE_URL_EN}/graphql", 
                                   json={'query': detail_query, 'variables': {'submissionId': int(sub['id'])}}, 
                                   headers=HEADERS).json()
            all_ac_records.append({
                "code": detail['data']['submissionDetails']['code'],
                "lang": sub['lang'],
                "id": sub['id']
            })
            time.sleep(0.2)
        return all_ac_records
    except: return []

# ================= 辅助功能 =================

def get_problem_details(slug):
    """获取元数据与中文描述"""
    q_meta = "query singleQuestion($titleSlug: String!) { question(titleSlug: $titleSlug) { questionId difficulty topicTags { name translatedName } } }"
    q_cn = "query translatedConfig($titleSlug: String!) { question(titleSlug: $titleSlug) { translatedTitle translatedContent } }"
    try:
        meta = requests.post(f"{BASE_URL_EN}/graphql", json={'query': q_meta, 'variables': {'titleSlug': slug}}, headers=HEADERS).json()['data']['question']
        cn = requests.post(f"{BASE_URL_CN}/graphql", json={'query': q_cn, 'variables': {'titleSlug': slug}}).json()['data']['question']
        return meta, cn
    except: return None, None

def ai_analyze(title, code):
    """GPT-4o 深度复盘"""
    # 遵循一句话本质的要求
    prompt = (
        f"分析算法题《{title}》的核心逻辑。\n"
        f"1. 一句话直击本质：用一句话总结该算法的核心逻辑。\n"
        f"2. 中文实现思路：描述解法步骤。\n"
        f"3. 伪代码：总结AC版本所有的通用解决方式/逻辑的中文伪代码。\n"
        f"4. 复杂度：使用 LaTeX 格式（如 $O(n)$）给出时间和空间复杂度。"
    )
    try:
        res = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt}], temperature=0.2)
        return res.choices[0].message.content
    except: return "AI 分析生成失败"

# ================= 主循环 =================

def main():
    if not os.path.exists("Problems"): os.makedirs("Problems")
    questions = get_all_ac_questions()

    # ⭐ 测试模式切片
    if TEST_MODE:
        print(f"🧪 测试模式开启：仅处理前 {TEST_LIMIT} 题")
        questions = questions[:TEST_LIMIT]
    
    for q in tqdm(questions, desc="🚀 同步中"):
        slug = q['titleSlug']
        meta, cn = get_problem_details(slug)
        if not meta: continue
        
        q_id = meta['questionId']
        folder = f"Problems/{q_id}_{slug}"
        
        # 断点续传逻辑
        if os.path.exists(f"{folder}/README_CN.md") and not TEST_MODE: 
            continue
        
        os.makedirs(folder, exist_ok=True)
        ac_records = get_all_accepted_codes(slug)
        
        if ac_records:
            # 保存所有 AC 代码
            for i, rec in enumerate(ac_records):
                ext = {"python": "py", "python3": "py", "java": "java", "cpp": "cpp"}.get(rec['lang'], "txt")
                with open(f"{folder}/solution_{i+1}.{ext}", 'w', encoding='utf-8') as f:
                    f.write(rec['code'])
            
            # 使用最新的一份代码进行 AI 分析
            analysis = ai_analyze(cn['translatedTitle'] if cn else slug, ac_records[0]['code'])
            
            with open(f"{folder}/README_CN.md", 'w', encoding='utf-8') as f:
                tags = " ".join([f"`{t['translatedName'] or t['name']}`" for t in meta['topicTags']])
                f.write(f"# {q_id}. {cn['translatedTitle'] if cn else slug}\n\n")
                f.write(f"**难度**: {meta['difficulty']} | **标签**: {tags}\n\n")
                f.write(f"## 题目描述\n\n{cn['translatedContent'] if cn else '暂无描述'}\n\n---\n")
                f.write(f"## 解解思路与复盘\n\n{analysis}")
            
            time.sleep(1)

    print(f"\n✅ {'测试' if TEST_MODE else '全量'}同步完成！")

if __name__ == "__main__":
    main()
