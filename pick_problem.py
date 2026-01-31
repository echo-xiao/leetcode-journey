import sys, json, random, os, re, html

def smart_clean_text(text):
    """深度清理：移除 HTML、NBSP、LaTeX 定界符及 Markdown 噪音"""
    if not text: return ""
    # 1. 解码 HTML 实体并处理各种特殊空格
    text = html.unescape(text)
    text = text.replace('\u00a0', ' ').replace('[NBSP]', ' ')
    
    # 2. 移除 LaTeX $ 符号 (手机端阅读噪音)
    text = text.replace('$', '')
    
    # 3. 移除图片、链接和 HTML 标签
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
    text = re.sub(r'</?[a-zA-Z][^>]*>', '', text)
    
    # 4. 移除 Markdown 装饰符
    text = re.sub(r'(\*\*|__|\*|_|~~|`|#+)', '', text)
    
    # 5. 压缩空行
    text = re.sub(r'\n{3,}', '\n\n', text).strip()
    return text

def select_problem(raw_input):
    data_file = 'summary.json'
    if not os.path.exists(data_file):
        print("Error: summary.json not found"); return

    with open(data_file, 'r', encoding='utf-8') as f:
        problems = json.load(f)
    
    # 核心优化：支持 "6. 图论算法" -> "图论" 的智能提取
    target = raw_input.split('.')[-1].strip() if '.' in raw_input else raw_input
    target = target.replace('算法', '').replace('常用', '') # 进一步精简关键字

    # 匹配逻辑：匹配分类名或标签
    matches = [
        p for p in problems 
        if target.lower() in p.get('category_main', '').lower() or 
           any(target.lower() in t.lower() for t in p.get('tags', []))
    ]
    
    if not matches:
        result = f"🔍 未找到与 '{target}' 相关的题目，已为您随机推荐。"
        p = random.choice(problems)
    else:
        p = random.choice(matches)

    prob_id, slug = str(p.get('id', '')), p.get('title_en', '')
    rel_path = f"Problems/{prob_id}_{slug}/README_CN.md"
    
    if os.path.exists(rel_path):
        with open(rel_path, 'r', encoding='utf-8') as f_md:
            raw_content = f_md.read()
            # 过滤掉 README 中的元数据部分，只保留核心内容
            clean_content = smart_clean_text(raw_content)
            result = f"【复习题目：#{prob_id} {p['title_cn']}】\n"
            result += f"难度：{p.get('difficulty', 'N/A')} | 分类：{p.get('category_main')}\n"
            result += "═" * 15 + "\n\n" + clean_content
    else:
        result = f"【题目：#{prob_id} {p['title_cn']}】\n内容文件缺失，请检查同步。"

    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"Successfully selected: {p['title_cn']}")

if __name__ == "__main__":
    # 接收来自 GitHub Action 的参数
    input_val = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].strip() else "Array"
    select_problem(input_val)
