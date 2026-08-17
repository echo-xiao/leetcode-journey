# 133. 克隆图 · 要素

1. 函数定义：dfs(curr, visited)：传入原图的一个节点和「原节点→克隆节点」的哈希表，返回 curr 对应的那份克隆节点（邻居也已接好）。

2. base case：两个：node 为空直接返回 None；curr 已在 visited 里就直接返回 visited[curr]，靠这个终止环形依赖。

3. 单层主体：先 new 一个值等于 curr.val 的 cloneNode 并立刻登记 visited[curr]=cloneNode，然后遍历 curr.neighbors，把每个邻居递归克隆的结果 append 到 cloneNode.neighbors。

4. 代码位置：前序位置：必须先建好克隆节点并写进哈希表，再去递归邻居，否则遇到环会无限递归。
