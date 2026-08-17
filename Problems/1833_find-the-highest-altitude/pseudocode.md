# 1833. 找到最高海拔 · 解题思路与伪代码

1. 一句话直击本质：通过累加海拔增量数组来计算每个点的海拔高度，并找出其中的最大值。

2. 综合思路：
   - 迭代法：遍历增量数组，逐步累加计算每个位置的海拔高度，并在过程中记录最大海拔。
   - 直接计算法：在遍历增量数组时，直接更新当前海拔高度，并同时更新最大海拔值。

3. 全量伪代码：
   ```plaintext
   方法1：迭代法
   输入：增量数组 gain
   初始化：当前海拔 curr_altitude = 0，最大海拔 max_altitude = 0
   对于每个增量值 g 在增量数组 gain 中：
       更新当前海拔 curr_altitude = curr_altitude + g
       如果 curr_altitude > max_altitude，则更新 max_altitude = curr_altitude
   返回 max_altitude

   方法2：直接计算法
   输入：增量数组 gain
   初始化：当前海拔 curr_altitude = 0，最大海拔 max_altitude = 0
   对于每个增量值 g 在增量数组 gain 中：
       更新当前海拔 curr_altitude = curr_altitude + g
       更新最大海拔 max_altitude = max(max_altitude, curr_altitude)
   返回 max_altitude
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是增量数组的长度，因为需要遍历整个数组一次。
   - 空间复杂度：$O(1)$，如果不存储每个位置的海拔高度，仅使用常数额外空间来存储当前和最大海拔。
