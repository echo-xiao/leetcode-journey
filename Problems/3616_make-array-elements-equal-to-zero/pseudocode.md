# 3616. 使数组元素等于零 · 解题思路与伪代码

1. **一句话直击本质：** 通过计算数组中每个零元素的前缀和与后缀和，判断是否可以通过左右移动使得数组元素全部变为零。

2. **综合思路：**
   - **前缀和与后缀和法：** 通过计算每个零元素的前缀和与后缀和，判断是否可以通过左右移动使得数组元素全部变为零。
   - **模拟移动法：** 对于每个零元素，模拟从该位置向左和向右移动，逐步减少非零元素，判断最终是否能使数组全部变为零。

3. **全量伪代码：**

   - **前缀和与后缀和法：**
     ```
     初始化计数器 cnt 为 0
     初始化前缀和数组 prefix 和后缀和数组 suffix 为长度为 n 的零数组
     对于每个索引 i 从 1 到 n-1：
         prefix[i] = prefix[i-1] + nums[i-1]
     对于每个索引 i 从 n-2 到 0：
         suffix[i] = suffix[i+1] + nums[i+1]
     对于每个索引 i 和对应的元素 num：
         如果 num 不等于 0，跳过
         如果 prefix[i] == suffix[i]，cnt 增加 2
         如果 abs(prefix[i] - suffix[i]) == 1，cnt 增加 1
     返回 cnt
     ```

   - **模拟移动法：**
     ```
     初始化计数器 cnt 为 0
     找到所有为零的元素的索引列表 start
     对于 start 中的每个索引 i：
         如果从 i 向右移动能使数组全为零，cnt 增加 1
         如果从 i 向左移动能使数组全为零，cnt 增加 1
     返回 cnt

     函数 to_left(start, nums, n):
         复制 nums 为 tmp
         初始化 curr 为 start，方向 direction 为 -1
         当 curr 在有效范围内：
             如果 tmp[curr] > 0，减少 tmp[curr]，反转方向，更新 curr
             否则，更新 curr
         返回 if_all_zeros(tmp)

     函数 to_right(start, nums, n):
         复制 nums 为 tmp
         初始化 curr 为 start，方向 direction 为 1
         当 curr 在有效范围内：
             如果 tmp[curr] > 0，减少 tmp[curr]，反转方向，更新 curr
             否则，更新 curr
         返回 if_all_zeros(tmp)

     函数 if_all_zeros(arr):
         对于 arr 中的每个元素 number：
             如果 number 不等于 0，返回 False
         返回 True
     ```

4. **复杂度：**

   - **前缀和与后缀和法：**
     - 时间复杂度：$O(n)$，因为需要遍历数组三次。
     - 空间复杂度：$O(n)$，因为需要存储前缀和和后缀和数组。

   - **模拟移动法：**
     - 时间复杂度：$O(n^2)$，因为对于每个零元素可能需要遍历整个数组。
     - 空间复杂度：$O(n)$，因为需要复制数组进行模拟。
