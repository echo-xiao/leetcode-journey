# 1498. 找出克隆二叉树中的相同节点 · 解题思路与伪代码

1. 一句话直击本质：通过同步遍历原始二叉树和克隆二叉树，找到与目标节点相同位置的节点。

2. 综合思路：
   - 递归深度优先搜索（DFS）：通过递归的方式同时遍历原始树和克隆树，检查当前节点是否为目标节点，如果是，则记录克隆树中对应节点。
   - 迭代深度优先搜索（DFS）：可以使用栈来模拟递归过程，逐步遍历树的节点。
   - 广度优先搜索（BFS）：可以使用队列来同时遍历原始树和克隆树的每一层，直到找到目标节点。

3. 全量伪代码：
   - 递归 DFS 版本：
     ```
     定义函数 getTargetCopy(original, cloned, target):
         初始化结果变量 res 为 None
         调用 dfs(original, cloned, target)
         返回 res

     定义函数 dfs(p, q, target):
         如果 p 或 q 为空，返回
         如果 p 是目标节点 target:
             将 q 赋值给结果变量 res
             返回
         递归调用 dfs(p.left, q.left, target)
         递归调用 dfs(p.right, q.right, target)
     ```

   - 迭代 DFS 版本（伪代码示例）：
     ```
     定义函数 getTargetCopy(original, cloned, target):
         初始化栈 stack，包含 (original, cloned)
         当栈不为空时:
             弹出栈顶元素 (p, q)
             如果 p 是目标节点 target:
                 返回 q
             如果 p.left 和 q.left 都不为空:
                 将 (p.left, q.left) 压入栈
             如果 p.right 和 q.right 都不为空:
                 将 (p.right, q.right) 压入栈
     ```

   - BFS 版本（伪代码示例）：
     ```
     定义函数 getTargetCopy(original, cloned, target):
         初始化队列 queue，包含 (original, cloned)
         当队列不为空时:
             取出队列头部元素 (p, q)
             如果 p 是目标节点 target:
                 返回 q
             如果 p.left 和 q.left 都不为空:
                 将 (p.left, q.left) 加入队列
             如果 p.right 和 q.right 都不为空:
                 将 (p.right, q.right) 加入队列
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都需要访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是二叉树的高度，递归调用栈或迭代使用的栈/队列的最大深度。对于平衡树，$h = O(\log n)$；对于非平衡树，$h = O(n)$。
