# 2843. 从 Rope 树中提取第 K 个字符

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Binary Tree`

## 题目描述

None

---
## 解题思路与复盘

1. 一句话直击本质：通过深度优先搜索（DFS）遍历 Rope 树，将所有叶子节点的字符串连接起来，然后直接访问第 K 个字符。

2. 综合思路：
   - 递归 DFS：通过递归的方式遍历 Rope 树，将每个叶子节点的字符串拼接成一个完整的字符串，然后直接访问第 K 个字符。
   - 迭代 DFS：可以使用栈来模拟递归的过程，达到同样的效果。
   - Rope 树特性：利用 Rope 树的特性，通过节点的长度信息直接定位到第 K 个字符，而不需要完整遍历所有字符。

3. 全量伪代码：
   - 递归 DFS 版本：
     ```
     定义函数 getKthCharacter(root, k):
         如果 root 为空，返回空
         初始化 res 为空字符串
         调用 dfs(root)
         返回 res 的第 k-1 个字符

     定义函数 dfs(node):
         如果 node 为空，返回
         递归调用 dfs(node.left)
         如果 node 是叶子节点，将 node.val 拼接到 res
         递归调用 dfs(node.right)
     ```
   - 迭代 DFS 版本（伪代码未提供，但可以推导）：
     ```
     定义函数 getKthCharacter(root, k):
         如果 root 为空，返回空
         初始化栈 stack
         初始化 res 为空字符串
         将 root 压入栈中
         当栈不为空时：
             弹出栈顶元素 node
             如果 node 是叶子节点，将 node.val 拼接到 res
             如果 node.right 不为空，将 node.right 压入栈
             如果 node.left 不为空，将 node.left 压入栈
         返回 res 的第 k-1 个字符
     ```
   - 利用 Rope 树特性（伪代码未提供，但可以推导）：
     ```
     定义函数 getKthCharacter(root, k):
         初始化当前节点 current 为 root
         当 current 不为空时：
             如果 k 小于等于 current.left.len：
                 current 移动到 current.left
             否则：
                 k 减去 current.left.len
                 如果 current 是叶子节点，返回 current.val 的第 k-1 个字符
                 否则，current 移动到 current.right
     ```

4. 复杂度：
   - 递归 DFS 版本：时间复杂度为 $O(n)$，空间复杂度为 $O(n)$，其中 $n$ 是树中节点的数量。
   - 迭代 DFS 版本：时间复杂度为 $O(n)$，空间复杂度为 $O(n)$。
   - 利用 Rope 树特性版本：时间复杂度为 $O(\log n)$，空间复杂度为 $O(1)$，假设树是平衡的。