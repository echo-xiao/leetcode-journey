import sys, json, random, os, re, html

def smart_clean_text(md_content):
    """提取纯文本并保护数学逻辑，移除图片和 HTML 标签"""
    if not md_content: return ""
    text = html.unescape(md_content)
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
    text = re.sub(r'<(p|br|div|h\d|section|ul|ol|li)>', '\n', text)
    text = re.sub(r'</?[a-zA-Z][^>]*>', '', text)
    text = re.sub(r'(\*\*|__|\*|_|~~|`|#+)', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text).strip()
    return text

def select_problem(tag_input):
    data_file = 'summary.json'
    
    if not os.path.exists(data_file):
        result = f"错误：未找到 {data_file}"
    else:
        with open(data_file, 'r', encoding='utf-8') as f:
            problems = json.load(f)
        
        # 匹配标签（不区分大小写）
        matches = [p for p in problems if any(tag_input.lower() in t.lower() for t in p.get('tags', []))]
        
        if matches:
            p = random.choice(matches)
            
            # --- 处理题号 ID ---
            # 你的 summary.json 中 id 是数字，所以这里强制转字符串
            prob_id = str(p.get('id', ''))
            id_str = f"#{prob_id} " if prob_id else ""
            
            # 解析路径：从 URL 提取相对路径
            # https://github.com/.../blob/main/Problems/0001-two-sum/README_CN.md
            url = p.get('url', '')
            rel_path = url.split('/blob/main/')[-1] if '/blob/main/' in url else ""
            
            if rel_path and os.path.exists(rel_path):
                with open(rel_path, 'r', encoding='utf-8') as f_md:
                    content = smart_clean_text(f_md.read())
                    # 组合最终展示内容
                    result = f"【复习题目：{id_str}{p['title']}】\n"
                    result += f"难度：{p.get('difficulty', 'N/A')}\n"
                    result += "=" * 25 + "\n\n"
                    result += content
            else:
                # 如果找不到本地文件，至少把题目和 ID 给出来
                result = f"【复习题目：{id_str}{p['title']}】\n(本地文件未找到: {rel_path})"
        else:
            result = f"未找到标签 '{tag_input}' 的题目。"

    # 写入结果文件供后续步骤（如发送消息）使用
    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write(result)

if __name__ == "__main__":
    target_tag = sys.argv[1] if len(sys.argv) > 1 else "Array"
    select_problem(target_tag)
