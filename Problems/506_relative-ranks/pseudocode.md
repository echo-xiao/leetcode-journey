# 506. 相对名次 · 解题思路与伪代码

1. **一句话直击本质：** 使用最大堆对分数进行排序，以确定每个分数的相对名次。

2. **综合思路：**
   - **最大堆排序法：** 将所有分数以负值形式插入最大堆中，以便按从大到小的顺序弹出元素，然后根据弹出顺序分配相应的名次（如金、银、铜牌或具体名次数字）。

3. **全量伪代码：**

   ```plaintext
   定义函数 findRelativeRanks(score):
       初始化空列表 maxHeap
       对于每个分数及其索引 (idx, val) 在 score 中:
           将 (-val, idx) 插入 maxHeap

       初始化结果列表 res，长度为 score 的长度
       初始化名次 place 为 1

       当 maxHeap 非空时:
           弹出 maxHeap 的顶部元素，获取其索引 pos
           如果 place 为 1:
               rank = "Gold Medal"
           否则如果 place 为 2:
               rank = "Silver Medal"
           否则如果 place 为 3:
               rank = "Bronze Medal"
           否则:
               rank = 转换 place 为字符串

           将 rank 赋值给 res[pos]
           place 增加 1

       返回 res
   ```

4. **复杂度：**

   - 时间复杂度：$O(n \log n)$，其中 $n$ 是分数列表的长度。构建最大堆和从堆中弹出元素的操作均为 $O(\log n)$，总共进行 $n$ 次。
   - 空间复杂度：$O(n)$，用于存储最大堆和结果列表。
