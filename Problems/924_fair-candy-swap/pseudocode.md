# 924. 公平的糖果交换 · 解题思路与伪代码

1. 一句话直击本质：通过计算两个数组的和的差值，找到一对元素交换使得两者的和相等。

2. 综合思路：
   - 哈希表法：通过计算两者和的差值，利用哈希表快速查找满足条件的元素对。
   - 数学推导法：通过数学公式推导出需要交换的元素对。

3. 全量伪代码：
   - 哈希表法：
     ```
     定义函数 fairCandySwap(aliceSizes, bobSizes):
         计算 suma 为 aliceSizes 的总和
         计算 sumb 为 bobSizes 的总和
         计算 sumt 为 (suma + sumb) / 2
         创建一个集合 seen 包含 bobSizes 的所有元素
         
         对于 aliceSizes 中的每个元素 i:
             计算 res 为 sumt - suma + i
             如果 res 在 seen 中:
                 返回 [i, res]
         返回 -1
     ```

4. 复杂度：
   - 时间复杂度：$O(n + m)$，其中 $n$ 是 `aliceSizes` 的长度，$m$ 是 `bobSizes` 的长度。
   - 空间复杂度：$O(m)$，用于存储 `bobSizes` 中的元素到集合 `seen`。
