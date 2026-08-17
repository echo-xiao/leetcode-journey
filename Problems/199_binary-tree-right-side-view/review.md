# 199. 二叉树的右视图 · 复盘

其实就是层序遍历返回最后一个res.append(vals[-1])，但是应该有最好的写法。bfs有三种方式：==**two queues、one queue + sentinel node、one queue + level size measurements、recursive dfs，dfs的逻辑比较有意思。**==dfs的思路更平常的不一样，是从右边开始，当level数字等于res的长度的时候，就append进去，因为这就意味着是这一层的第一个。len(res)是0，说明第0层还没填。
