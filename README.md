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

它按顺序做七件事，顺序不能调换——题目得先存在，复盘才有地方放；
回顾表的行得先建好，复盘列才写得进去；app 的内容包必须最后打包，
不然打包时 `Problems/*/review.md` 还是上一轮的，手机上拿到的就是旧内容：

1. 刷新最近重刷过的题目的通过时间
2. 拉力扣上新通过的题，生成四件套，并在 Notion「LC 旧题回顾」建行
3. 刷新写法变了的老题：拿力扣最近 20 条 AC，比对每道题的代码结构，只有出现了本地
   没有的写法才重下代码、重生成伪代码和要素。改个变量名不算，换一种解法才算
4. 给新题生成要素答案（每题一次 Claude 调用）
5. 把 Notion 上的复盘写进各题的 `review.md`
6. 把复盘写进「LC 旧题回顾」的复盘列，橙色高亮一并带过去
7. 把 `Problems/` 打包成 `app/content.json`，供 iOS app 下载

### 不用手动跑

`scripts/sync_daily.sh` 每天凌晨 3:00 由 launchd 自动跑一遍上面这条管线，跑完只提交
`Problems/`、`app/content.json`、`lc_review/data_elements/` 并推送。Mac 睡着不会跳过，
醒来后补跑一次。日志在 `logs/`，留 14 天。

失败会弹一条 macOS 通知，成功不弹。最常见的失败是力扣 session 过期，几周一次，重新在
Chrome 登录把 cookie 填回 `.env` 就行。另一种是当时不在 `main` 分支上——定时任务会拒绝
在别的分支上提交，直接跳过并通知。

装：

```bash
ln -sf "$PWD/scripts/com.echoxiao.leetcode-journey.sync.plist" \
   ~/Library/LaunchAgents/com.echoxiao.leetcode-journey.sync.plist
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.echoxiao.leetcode-journey.sync.plist
```

停：

```bash
launchctl bootout gui/$(id -u)/com.echoxiao.leetcode-journey.sync
```

不加 `--apply` 是试运行，只报告会做什么，不写任何东西，包括最后一步的
`app/content.json`。前四步里有三步写到工作区之外（Notion 没有撤销），
所以写入是显式的。

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

## 手机 app 的内容

```bash
python3 -m lc_review.cli export-app
```

生成 `app/content.json`：每道题的题面、要素、伪代码、复盘、真代码打成一个文件，
iOS app 启动时从 GitHub Raw 拉这一份。已挂进 `sync-all` 的最后一步。

**这个文件必须提交并推送**，和 `anki/` 相反。GitHub Raw 只能服务已经提交的文件，
所以生成物在这里是个刻意的例外，别把 `app/` 加进 `.gitignore`。文件生成了但没推，
手机上拿到的就还是旧内容，而且不会有任何报错提示你。

内容没变时命令不会重写文件，所以每天跑 `sync-all` 不会制造空 diff。

## 手机 app

`app/ios/LCReview.xcodeproj`，SwiftUI，iOS 17 起，零第三方依赖。

Xcode 打开、选自己的 iPhone、Run 就装上了。它启动时从 GitHub Raw 拉
`app/content.json`，所以加了新题只要 `sync-all` 完再 push 就行，不用重装 app。
（GitHub Raw 有 CDN 缓存，push 后几分钟才生效。）

复习状态存在手机本地，不上云、不要账号。删掉 app 会丢排期，题目内容不会丢——
重装后重新下载即可。

首页的热力图和连续天画的是 LeetCode 的提交记录，app 每次回到前台直接去
`leetcode.com/graphql` 拉，不经过这个仓库。格子的深浅是那天的提交次数，和
leetcode.com 个人主页上那张图一致；日期按 UTC 分天，所以最右边一格可能和本地的
"今天"差一天——这是照搬，不是 bug，接口只给按天聚合的结果，没法准确矫正。

拉不到就画上一次成功的结果，并在上方标注"数据截至 X月X日"；从来没拉到过则画空
网格，写"暂时拿不到 LeetCode 数据"。两种文案不一样是刻意的：都画成空格子的话，
"没数据"会被读成"没刷题"。

这是 app 唯一一个 GitHub 之外的外部依赖，LeetCode 改了接口的话热力图会静默停在
缓存上，不会有任何报错。

「复习」那个计数仍然来自 app 自己的打分记录，那是 LeetCode 不知道的部分。

跑测试：

```bash
cd app/ios
xcodebuild test -scheme LCReview -destination 'platform=iOS Simulator,name=iPhone 12 mini'
```

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
