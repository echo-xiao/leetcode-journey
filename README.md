# leetcode-journey

我的力扣刷题记录：代码、题目、思路、要素、复盘，每题一个文件夹。

## 每道题有什么

```
Problems/104_maximum-depth-of-binary-tree/
  README_CN.md    索引：难度、标签、指向下面几个文件
  problem.md      题目描述
  pseudocode.md   一句话本质 / 综合思路 / 全量伪代码 / 复杂度
  elements.md     这道题的要素——下笔前必须先填的几个空
  review.md       我自己的复盘，标黄的是当时卡住的地方
  solution_*.py   每一版 AC 代码
```

`elements.md` 的槽位按题型统一维护（18 个题型，定义在 `lc_review/element_essentials.py`），
答案是逐题填的。比如二叉树类的四个槽位是：函数定义、base case、单层主体、代码位置。

## 日常怎么用

刷完题、在 Notion 上写完复盘，跑一条：

```bash
python3 -m lc_review.cli sync-all --apply
```

它按顺序做四件事，顺序不能调换——题目得先存在，复盘才有地方放；
回顾表的行得先建好，复盘列才写得进去：

1. 拉力扣上新通过的题，生成四件套，并在 Notion「LC 旧题回顾」建行
2. 给新题生成要素答案（每题一次 Claude 调用）
3. 把 Notion 上的复盘写进各题的 `review.md`
4. 把复盘写进「LC 旧题回顾」的复盘列，橙色高亮一并带过去

不加 `--apply` 是试运行，只报告会做什么，不写任何东西。四步里有三步写到工作区之外
（Notion 没有撤销），所以写入是显式的。

单独跑某一步：

```bash
python3 -m lc_review.cli sync-new --apply        # 只拉新题
python3 -m lc_review.cli build-answers --apply   # 只补要素答案
python3 -m lc_review.cli sync-review-md --apply  # 只更新 review.md
python3 -m lc_review.cli sync-fupan --apply      # 只更新 Notion 复盘列
```

## 刷卡

```bash
python3 -m lc_review.cli export-anki
```

生成 `anki/elements.tsv`，Anki 里 File → Import 导入，牌组是 `LeetCode::要素`，
一题一张：正面题目，背面这道题的要素怎么填。标签按题型打好，可以只刷某一类。

`anki/` 不进版本库——它是从 `Problems/` 生成的，重跑一条命令就有。

## 需要配置什么

`.env`（已在 `.gitignore` 里，不会进版本库）：

```
LEETCODE_SESSION=...     # Chrome 登录 leetcode.com 后的 cookie
LEETCODE_CSRFTOKEN=...
CLAUDE_TOKEN=sk-ant-...  # 生成思路和要素答案
NOTION_TOKEN=ntn_...     # Notion 内部集成，需把两个数据库分享给它
```

LeetCode 的 session 隔几周会过期。过期后接口不会报错，而是返回 0 道通过题——
所以 `sync-new` 会先验证，拿到空用户名就直接报错退出，不会静默空跑。
重新在 Chrome 登录 leetcode.com，把新的 cookie 填回 `.env` 即可。

## 复盘是怎么进来的

复盘写在 Notion 的两个页面里，格式是流水账：

- easy 页：`20、valid parentheses：正文`
- medium 页：`3、LC 1004 最大连续1的个数III：正文`，按 `--- Day N | 主题 ---` 分段

`lc_review/fupan.py` 负责解析，橙色高亮会被单独抽出来——那是我自己标的易错点。
写进 md 时转成 `==高亮==`（GitHub 渲染成黄色底），写进 Notion 时还原成橙色。

## 目录

```
lc_review/          全部逻辑
  cli.py            命令入口
  leetcode_api.py   力扣抓取 + Claude 生成分析
  fupan.py          复盘页解析
  notion_api.py     Notion REST 客户端
  notion_pages.py   把 Notion 页面还原成解析器认识的文本
  sync_new.py       新题 -> Problems/ + Notion 建行
  sync_review_md.py 复盘 -> review.md
  sync_fupan.py     复盘 -> Notion 复盘列
  elements_*.py     要素答案的生成与渲染
  element_essentials.py  18 个题型的要素定义（唯一来源）
tests/              pytest
Problems/           每题一个文件夹
```
