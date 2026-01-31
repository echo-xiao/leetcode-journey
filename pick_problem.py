import sys, json, random, os, re, html

def smart_clean_text(text):
    """清理所有 [NBSP]、美元符号和 HTML 噪音"""
    if not text: return ""
    text = html.unescape(text)
    # 物理清理特殊空格和 LaTeX 符号
    text = text.replace('\u00a0', ' ').replace('[NBSP]', ' ').replace('$', '')
    # 移除 HTML 标签和图片
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'</?[a-zA-Z][^>]*>', '', text)
    # 移除 Markdown 装饰符
    text = re.sub(r'(\*\*|__|\*|_|~~|`|#+)', '', text)
    return text.strip()

def select_problem(raw_input):
    # 强制校验：如果没传参，直接输出错误，不再默认 Array
    if not raw_input or raw_input.strip() == "":
        with open('result.txt', 'w', encoding='utf-8') as f:
            f.write("❌ 错误：GitHub Action 未接收到分类参数，请检查 Shortcuts 的 Payload 配置。")
        return

    data_file = 'summary.json'
    with open(data_file, 'r', encoding='utf-8') as f:
        problems = json.load(f)
    
    # 智能匹配：从 "4. 网格图" 提取 "网格图"
    keyword = raw_input.split('.')[-1].strip()
    
    matches = [
        p for p in problems 
        if keyword.lower() in p.get('category_main', '').lower() or 
           any(keyword.lower() in t.lower() for t in p.get('tags', []))
    ]
    
    if not matches:
        with open('result.txt', 'w', encoding='utf-8') as f:
            f.write(f"🔍 匹配失败：在库中找不到分类 [{keyword}]。参数原文: {raw_input}")
        return

    p = random.choice(matches)
    path = f"Problems/{p['id']}_{p['title_en']}/README_CN.md"
    
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f_md:
            content = smart_clean_text(f_md.read())
            result = f"【复习：#{p['id']} {p['title_cn']}】\n分类：{p['category_main']}\n"
            result += "═" * 15 + "\n\n" + content
    else:
        result = f"❌ 文件缺失: {path}"

    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write(result)

if __name__ == "__main__":
    # 接收参数
    val = sys.argv[1] if len(sys.argv) > 1 else ""
    select_problem(val)
