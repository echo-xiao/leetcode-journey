import sys, json, random, os, re, html

def smart_clean_text(text):
    """最强清理：强制剔除 [NBSP]、美元符号、HTML 标签"""
    if not text: return ""
    # 1. 解码并替换特殊空格
    text = html.unescape(text)
    text = text.replace(" ", " ").replace("[NBSP]", " ")
    
    # 2. 移除 LaTeX 符号 $ (直接物理移除)
    text = text.replace("$", "")
    
    # 3. 移除图片和 HTML 标签
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    text = re.sub(r"</?[a-zA-Z][^>]*>", "", text)
    
    # 4. 移除 Markdown 装饰符 (如 **加粗**)
    text = re.sub(r"(\*\*|__|\*|_|~~|`|#+)", "", text)
    
    # 5. 压缩空行
    return re.sub(r"
{3,}", "

", text).strip()

def select_problem(raw_input):
    data_file = "summary.json"
    if not os.path.exists(data_file):
        print("Error: summary.json not found"); return

    with open(data_file, "r", encoding="utf-8") as f:
        problems = json.load(f)

    # --- 智能匹配逻辑 ---
    # 过滤掉输入和 JSON 分类中的数字、空格、点号，只比对文字
    def normalize(s):
        return re.sub(r"[\d\.\s]", "", s).lower()

    # 修改匹配部分的代码
    target = normalize(raw_input)
    
    matches = []
    for p in problems:
        category_name = normalize(p.get("category_main", ""))
        tags = [normalize(t) for t in p.get("tags", [])]
        
        # 只要 target 包含分类名，或者分类名包含 target，就视为匹配
        if (target in category_name or category_name in target or 
            any(target in t or t in target for t in tags)):
            matches.append(p)
    
    if not matches:
        # 调试：如果匹配失败，把库里前两个分类写进结果，帮你排查
        sample = [p.get("category_main") for p in problems[:2]]
        error_msg = f"🔍 匹配失败
输入内容: {raw_input}
转换关键字: {target}
库中首个分类: {sample}"
        with open("result.txt", "w", encoding="utf-8") as f: f.write(error_msg)
        return

    p = random.choice(matches)
    # 路径拼接：Problems/{id}_{title_en}/README_CN.md
    path = f"Problems/{p["id"]}_{p["title_en"]}/README_CN.md"
    
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f_md:
            raw_content = f_md.read()
            # 执行深度清洗
            content = smart_clean_text(raw_content)
            
            result = f"【复习：#{p["id"]} {p["title_cn"]}】
"
            result += f"难度：{p["difficulty"]} | 归类：{p["category_main"]}
"
            result += "═" * 15 + "

" + content
    else:
        result = f"❌ 找到题目但文件缺失: {path}"

    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(result)

if __name__ == "__main__":
    # 接收来自 Shortcuts -> GitHub Action 的参数
    val = sys.argv[1] if len(sys.argv) > 1 else ""
    select_problem(val)
