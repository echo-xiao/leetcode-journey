# 3702. 最长乘积等价子数组

**难度**: Easy | **标签**: `Array` `Math` `Sliding Window` `Enumeration` `Number Theory`

## 题目描述

<p>给你一个由&nbsp;<strong>正整数&nbsp;</strong>组成的数组 <code>nums</code>。</p>

<p>如果一个数组 <code>arr</code> 满足 <code>prod(arr) == lcm(arr) * gcd(arr)</code>，则称其为&nbsp;<strong>乘积等价数组&nbsp;</strong>，其中：</p>

<ul>
	<li><code>prod(arr)</code> 表示 <code>arr</code> 中所有元素的乘积。</li>
	<li><code>gcd(arr)</code> 表示 <code>arr</code> 中所有元素的最大公因数 (<span data-keyword="gcd-function">GCD</span>)。</li>
	<li><code>lcm(arr)</code> 表示 <code>arr</code> 中所有元素的最小公倍数 (<span data-keyword="lcm-function">LCM</span>)。</li>
</ul>

<p>返回数组 <code>nums</code> 的&nbsp;<strong>最长</strong> <strong>乘积等价 <span data-keyword="subarray-nonempty">子数组</span>&nbsp;</strong>的长度。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,1,2,1,1,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong>&nbsp;</p>

<p>最长的乘积等价子数组是 <code>[1, 2, 1, 1, 1]</code>，其中&nbsp;<code>prod([1, 2, 1, 1, 1]) = 2</code>，&nbsp;<code>gcd([1, 2, 1, 1, 1]) = 1</code>，以及&nbsp;<code>lcm([1, 2, 1, 1, 1]) = 2</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [2,3,4,5,6]</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong>&nbsp;</p>

<p>最长的乘积等价子数组是 <code>[3, 4, 5]</code>。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3,1,4,5,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过计算子数组的乘积、最小公倍数和最大公约数，或通过质因子分解和滑动窗口，找到满足条件的最长子数组。

2. **综合思路：**
   - **版本 1 和 2：** 使用双重循环遍历所有可能的子数组，计算每个子数组的乘积、最小公倍数和最大公约数，判断乘积是否等于最小公倍数与最大公约数的乘积。
   - **版本 3：** 通过预计算最小质因子，使用滑动窗口和质因子分解来寻找最长的两两互质子数组。

3. **全量伪代码：**
   - **双重循环方法：**
     ```
     初始化结果 res 为 1
     对于每个起始位置 left 从 0 到 n-1：
         初始化 g, l, p 为 nums[left]
         对于每个结束位置 right 从 left+1 到 n-1：
             更新 p 为 p * nums[right]
             更新 l 为 lcm(l, nums[right])
             更新 g 为 gcd(g, nums[right])
             如果 p 等于 l * g：
                 更新 res 为 max(res, right - left + 1)
     返回 res
     ```
   - **质因子分解与滑动窗口方法：**
     ```
     如果数组为空，返回 0
     如果数组长度为 1，返回 1 如果 nums[0] 为 1，否则返回 0
     预计算每个数的最小质因子 (SPF)
     定义辅助函数 get_prime_factors(num) 获取数的所有唯一质因子
     初始化滑动窗口的左边界 left 为 0
     初始化最大长度 max_pairwise_coprime_len 为 0
     对于每个右边界 right 从 0 到 n-1：
         获取 nums[right] 的质因子并更新计数
         如果窗口内有共享质因子，收缩左边界
         更新 max_pairwise_coprime_len 为 max(max_pairwise_coprime_len, right - left + 1)
     返回 max(max_pairwise_coprime_len, 2)
     ```

4. **复杂度：**
   - **版本 1 和 2 时间复杂度：** $O(n^2 \log(\max(nums)))$，空间复杂度：$O(1)$。
   - **版本 3 时间复杂度：** $O(n \log(\max(nums)))$，空间复杂度：$O(\max(nums))$。