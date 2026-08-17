# 637. 二叉树的层平均值 · 解题思路与伪代码

1. **一句话直击本质：** 通过层序遍历（BFS）或递归（DFS）遍历二叉树，计算每一层节点值的平均值。

2. **综合思路：**
   - **递归（DFS）解法：** 使用递归遍历二叉树的每一层，维护一个列表来记录每层的节点值总和和节点数量，最后计算平均值。
   - **迭代（BFS）解法：** 使用队列进行层序遍历，逐层计算节点值总和和节点数量，最后计算平均值。

3. **全量伪代码：**

   - **递归（DFS）解法：**
     ```
     定义函数 averageOfLevels(root):
         如果 root 为空，返回空列表
         初始化 stats 列表用于存储每层的总和和节点数量
         调用 traverse(root, 0)
         返回 stats 中每层总和除以节点数量的结果列表

     定义递归函数 traverse(node, depth):
         如果 node 为空，返回
         如果 depth 等于 stats 的长度，向 stats 添加一个新的 [0, 0] 列表
         stats[depth][0] 增加 node.val
         stats[depth][1] 增加 1
         递归调用 traverse(node.left, depth + 1)
         递归调用 traverse(node.right, depth + 1)
     ```

   - **迭代（BFS）解法：**
     ```
     定义函数 averageOfLevels(root):
         如果 root 为空，返回空列表
         初始化队列 q 并将 root 加入队列
         初始化 res 列表用于存储每层的平均值
         当队列 q 不为空时:
             记录当前队列的大小 sz
             初始化 ttl 为 0
             遍历当前层的每个节点:
                 从队列中弹出节点 cur
                 ttl 增加 cur.val
                 如果 cur.left 不为空，将 cur.left 加入队列
                 如果 cur.right 不为空，将 cur.right 加入队列
             将 ttl 除以 sz 的结果加入 res
         返回 res
     ```

4. **复杂度：**
   - **时间复杂度：** $O(n)$，其中 $n$ 是二叉树中的节点总数，因为每个节点都被访问一次。
   - **空间复杂度：** $O(m)$，其中 $m$ 是二叉树的最大宽度（即某一层的最大节点数），用于存储队列或递归调用栈。
