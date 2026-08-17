# 3610. 计算子数组的 x-sum I · 解题思路与伪代码

1. **一句话直击本质：** 通过滑动窗口和最小堆或排序，计算每个子数组中频率最高的前 x 个元素的加权和。

2. **综合思路：**
   - **滑动窗口与最小堆：** 对于每个长度为 k 的子数组，使用字典统计元素频率，然后使用最小堆维护频率最高的 x 个元素，最后计算这些元素的加权和。
   - **滑动窗口与排序：** 对于每个长度为 k 的子数组，使用 `Counter` 统计元素频率，然后对频率进行排序，选择前 x 个频率最高的元素计算加权和。

3. **全量伪代码：**

   ```plaintext
   初始化结果列表 res
   对于每个可能的子数组起始索引 i 从 0 到 n-k:
       取出当前子数组 newNums = nums[i: i+k]
       初始化频率字典 mapp
       对于子数组中的每个元素 num:
           更新 mapp 中 num 的频率
       
       初始化一个最小堆 minHeap
       对于 mapp 中的每个元素及其频率 (val, freq):
           如果 minHeap 的大小小于 x:
               将 (freq, val) 插入 minHeap
           否则:
               将 (freq, val) 插入 minHeap 并弹出最小元素

       初始化当前子数组的和 summ = 0
       对于 minHeap 中的每个元素 (freq, val):
           summ 增加 freq * val
       
       将 summ 添加到结果列表 res

   返回结果列表 res
   ```

   或者：

   ```plaintext
   初始化结果列表 res_arr
   对于每个可能的子数组起始索引 l 从 0 到 n-k:
       取出当前子数组 win = nums[l: l+k]
       使用 Counter 统计 win 中的元素频率 counts
       初始化当前子数组的和 res = 0
       
       如果 counts 的长度小于 x:
           res = win 中所有元素的和
       否则:
           将 counts 转换为列表 freq
           按照频率和元素值对 freq 进行降序排序
           取出前 x 个元素 top
           对于 top 中的每个元素 (n, f):
               res 增加 n * f

       将 res 添加到结果列表 res_arr

   返回结果列表 res_arr
   ```

4. **复杂度：**

   - 时间复杂度：$O((n-k+1) \cdot (k + x \log x))$，其中 $n$ 是数组的长度，$k$ 是子数组的长度，$x$ 是需要计算的频率最高的元素个数。
   - 空间复杂度：$O(k + x)$，用于存储子数组和最小堆。
