# 433. 最小基因变化 · 解题思路与伪代码

1. 一句话直击本质：该算法使用广度优先搜索（BFS）在基因序列的变化路径中寻找从起始基因到目标基因的最短变化序列。

2. 综合思路：
   - 广度优先搜索（BFS）：使用队列来逐层遍历可能的基因变化，从起始基因开始，每次改变一个字符，检查是否能到达目标基因，确保找到最短路径。
   - 数据结构：使用集合来存储基因库以便快速查找，使用队列来实现广度优先搜索，使用集合来跟踪已访问的基因以避免重复访问。

3. 全量伪代码：
   ```
   定义函数 minMutation(startGene, endGene, bank)
       将 bank 转换为集合 bank_set
       如果 endGene 不在 bank_set 中
           返回 -1

       初始化队列 queue，包含元组 (startGene, 0)
       初始化集合 visited，包含 startGene

       当队列 queue 不为空时
           弹出队列的第一个元素，赋值给 curr 和 step

           如果 curr 等于 endGene
               返回 step

           对于 curr 中的每个字符位置 i
               对于字符集合 'ACGT' 中的每个字符 char
                   生成新的基因序列 nxt_gene
                   如果 nxt_gene 在 bank_set 中且不在 visited 中
                       将 nxt_gene 添加到 visited
                       将 (nxt_gene, step+1) 添加到队列 queue

       返回 -1
   ```

4. 复杂度：
   - 时间复杂度：$O(N \times M \times 4)$，其中 $N$ 是基因序列的长度，$M$ 是基因库的大小，4 是每个位置可能的字符变化数。
   - 空间复杂度：$O(M)$，用于存储基因库集合和访问集合。
