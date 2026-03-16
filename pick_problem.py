import sys, json, random, os, re, html

def smart_clean_text(text):
    """最强清理：强制剔除 [NBSP]、美元符号、HTML 标签"""
    if not text: return ""
    text = html.unescape(text)
    text = text.replace('\u00a0', ' ').replace('[NBSP]', ' ')
    text = text.replace('$', '')
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'</?[a-zA-Z][^>]*>', '', text)
    text = re.sub(r'(\*\*|__|\*|_|~~|`|#+)', '', text)
    return re.sub(r'\n{3,}', '\n\n', text).strip()

def select_problem(raw_input):
    data_file = 'summary.json'
    if not os.path.exists(data_file):
        print("Error: summary.json not found"); return

    with open(data_file, 'r', encoding='utf-8') as f:
        problems = json.load(f)

    def normalize(s):
        return re.sub(r'[\d\.\s]', '', s).lower()

    target = normalize(raw_input)

    matches = []
    for p in problems:
        category_name = normalize(p.get('category_main', ''))
        tags = [normalize(t) for t in p.get('tags', [])]
        if (target in category_name or category_name in target or
                any(target in t or t in target for t in tags)):
            matches.append(p)

    if not matches:
        sample = [p.get('category_main') for p in problems[:2]]
        error_msg = '🔍 匹配失败\n输入内容: ' + raw_input + '\n转换关键字: ' + target + '\n库中首个分类: ' + str(sample)
        with open('result.txt', 'w', encoding='utf-8') as f:
            f.write(error_msg)
        return

    p = random.choice(matches)
    pid = p['id']
    title_en = p['title_en']
    title_cn = p['title_cn']
    difficulty = p['difficulty']
    category_main = p['category_main']
    path = 'Problems/' + str(pid) + '_' + title_en + '/README_CN.md'

    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f_md:
            raw_content = f_md.read()
            content = smart_clean_text(raw_content)
            result = '【复习：#' + str(pid) + ' ' + title_cn + '】\n'
            result += '难度：' + difficulty + ' | 归类：' + category_main + '\n'
            result += '═' * 15 + '\n\n' + content
    else:
        result = '❌ 找到题目但文件缺失: ' + path

    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write(result)

if __name__ == '__main__':
    val = sys.argv[1] if len(sys.argv) > 1 else ''
    select_problem(val)
