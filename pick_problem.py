import sys, json, random, os, re, html


def smart_clean_text(md_content):
    """提取纯文本，清理 HTML、Markdown 符号、[NBSP] 及 $ 定界符"""
    if not md_content: return ""

    # 1. 处理 HTML 实体转义并替换特殊空格 (NBSP)
    text = html.unescape(md_content)
    text = text.replace('\u00a0', ' ')  # 替换 Unicode NBSP
    text = text.replace('[NBSP]', ' ')  # 替换字面量标记

    # 2. 移除图片和链接格式
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)

    # 3. 移除 HTML 标签并处理换行
    text = re.sub(r'<(p|br|div|h\d|section|ul|ol|li)>', '\n', text)
    text = re.sub(r'</?[a-zA-Z][^>]*>', '', text)

    # 4. 核心：移除 Markdown 装饰符及 $ 符号
    # 增加对 $ 的过滤
    text = re.sub(r'(\*\*|__|\*|_|~~|`|#+|\$)', '', text)

    # 5. 清理多余空行
    text = re.sub(r'\n{3,}', '\n\n', text).strip()
    return text


def select_problem(tag_input):
    data_file = 'summary.json'
    if not os.path.exists(data_file):
        result = "❌ 未找到 summary.json"
    else:
        with open(data_file, 'r', encoding='utf-8') as f:
            problems = json.load(f)

        # 匹配逻辑
        matches = [p for p in problems if any(tag_input.lower() in t.lower() for t in p.get('tags', []))
                   or tag_input.lower() in p.get('category_main', '').lower()]

        if matches:
            p = random.choice(matches)
            prob_id, slug = str(p.get('id', '')), p.get('title_en', '')
            rel_path = f"Problems/{prob_id}_{slug}/README_CN.md"

            if os.path.exists(rel_path):
                with open(rel_path, 'r', encoding='utf-8') as f_md:
                    # 清理后的内容
                    content = smart_clean_text(f_md.read())
                    result = f"【复习题目：#{prob_id} {p['title_cn']}】\n"
                    result += f"难度：{p.get('difficulty', 'N/A')}\n"
                    result += "=" * 25 + "\n\n" + content
            else:
                result = f"【复习题目：#{prob_id} {p['title_cn']}】\n(文件缺失)"
        else:
            result = f"🔍 未找到 '{tag_input}' 相关题目"

    print(result)
    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write(result)


if __name__ == "__main__":
    target_tag = sys.argv[1] if len(sys.argv) > 1 else "Array"
    select_problem(target_tag)