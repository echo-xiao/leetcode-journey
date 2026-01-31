import sys, json, random, os, re, html

def smart_clean_text(text):
    """最强清理：强制剔除 [NBSP]、美元符号、HTML 标签"""
    if not text: return ""
    # 1. 解码并替换特殊空格
    text = html.unescape(text)
    text = text.replace('\u00a0', ' ').replace('[NBSP]', ' ')
    
    # 2. 移除 LaTeX 符号 $ (直接物理移除)
    text = text.replace('$', '')
    
    # 3. 移除图片和 HTML 标签
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'</?[a-zA-Z][^>]*>', '', text)
    
    # 4. 移除 Markdown 装饰符 (如 **加粗**)
    text = re.sub(r'(\*\*|__|\*|_|~~|`|#+)', '', text)
    
    # 5. 压缩空行
    return re.sub(r'\n{3,}', '\n\n', text).strip()

def select_problem(raw_input):
    data_file = 'summary.json'
    if not os.path.exists(data_file):
        print("Error: summary.json not found"); return

    with open(data_file, 'r', encoding='utf-8') as f:
        problems = json.load(f)

    # --- 智能匹配逻辑 ---
    # 过滤掉输入和 JSON 分类中的数字、空格、点号，只比对文字
    def normalize(s):
        return re.sub(r'[\d\.\s]', '', s).lower()

    target = normalize(raw_input)
    
    # 在 summary.json 中匹配 category_main 或 tags
    matches = [
        p for p in problems 
        if target in normalize(p.get('category_main', '')) or 
           any(target in normalize(t) for t in p.get('tags', []))
    ]
    
    if not matches:
        # 调试：如果匹配失败，把库里前两个分类写进结果，帮你排查
        sample = [p.get('category_main') for p in problems[:2]]
        error_msg = f"🔍 匹配失败\n输入内容: {raw_input}\n转换关键字: {target}\n库中首个分类: {sample}"
        with open('result.txt', 'w', encoding='utf-8') as f: f.write(error_msg)
        return

    p = random.choice(matches)
    # 路径拼接：Problems/{id}_{title_en}/README_CN.md
    path = f"Problems/{p['id']}_{p['title_en']}/README_CN.md"
    
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f_md:
            raw_content = f_md.read()
            # 执行深度清洗
            content = smart_clean_text(raw_content)
            
            result = f"【复习：#{p['id']} {p['title_cn']}】\n"
            result += f"难度：{p['difficulty']} | 归类：{p['category_main']}\n"
            result += "═" * 15 + "\n\n" + content
    else:
        result = f"❌ 找到题目但文件缺失: {path}"

    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write(result)

if __name__ == "__main__":
    # 接收来自 Shortcuts -> GitHub Action 的参数
    val = sys.argv[1] if len(sys.argv) > 1 else ""
    select_problem(val)
