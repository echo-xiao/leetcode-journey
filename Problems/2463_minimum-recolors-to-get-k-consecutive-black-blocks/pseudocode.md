# 2463. 得到 K 个黑块的最少涂色次数 · 解题思路与伪代码

1. 一句话直击本质：使用滑动窗口技术计算每个长度为 K 的子串中白块的最小数量。

2. 综合思路：
   - 滑动窗口：通过维护一个长度为 K 的滑动窗口，计算窗口内白块的数量，并在窗口滑动时更新计数，寻找最小值。

3. 全量伪代码：
   ```plaintext
   定义函数 minimumRecolors(blocks, k):
       初始化 n 为 blocks 的长度
       初始化 i 为 0
       初始化 cnt 为 0
       初始化 min_cnt 为一个很大的数
       初始化 win 为 blocks 的前 k 个字符
       
       对于 win 中的每个字符 e:
           如果 e 是 'W':
               cnt 增加 1
       将 min_cnt 更新为 cnt 和 min_cnt 的较小值

       对于 j 从 k 到 n-1:
           将 win 更新为 blocks 从 i+1 到 i+k+1 的子串
           如果 blocks[j] 是 'W':
               cnt 增加 1
           如果 blocks[i] 是 'W':
               cnt 减少 1
           将 min_cnt 更新为 cnt 和 min_cnt 的较小值
           i 增加 1
       
       返回 min_cnt
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，因为每个字符最多被访问两次。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外变量。
