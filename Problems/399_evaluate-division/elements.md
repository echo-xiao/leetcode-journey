# 399. 除法求值 · 要素

1. union 连谁：每条方程 equations[i]=(u,v) 里的变量 u 和 v 做 union，并把权重 weight[rootU] 更新为 val 乘以对应的比例系数，使得 u/v=val 关系体现在带权并查集里

2. connected 判据：先分别找到 u 和 v 的根节点 rootU、rootV，如果两个变量不在 parent 字典里说明没出现过直接判不连通返回-1，否则看 rootU 是否等于 rootV，相等就是连通的，可以用 weight[u]/weight[v] 算出比值

3. 优化方式：要做路径压缩，在 find 函数里递归查找根节点时把路径上每个节点的 parent 直接指向根节点，同时同步更新 weight 为该节点到根节点的累计比值，本题没有按秩合并（union 时统一把一方根接到另一方根即可，量级不大不影响效率）
