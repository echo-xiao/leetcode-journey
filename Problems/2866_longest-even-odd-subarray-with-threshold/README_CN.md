# 2866. 最长奇偶子数组

**难度**: Easy | **标签**: `Array` `Sliding Window`

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 和一个整数 <code>threshold</code> 。</p>

<p>请你从 <code>nums</code> 的子数组中找出以下标 <code>l</code> 开头、下标 <code>r</code> 结尾 <code>(0 &lt;= l &lt;= r &lt; nums.length)</code> 且满足以下条件的 <strong>最长子数组</strong> ：</p>

<ul>
	<li><code>nums[l] % 2 == 0</code></li>
	<li>对于范围&nbsp;<code>[l, r - 1]</code> 内的所有下标 <code>i</code> ，<code>nums[i] % 2 != nums[i + 1] % 2</code></li>
	<li>对于范围&nbsp;<code>[l, r]</code> 内的所有下标 <code>i</code> ，<code>nums[i] &lt;= threshold</code></li>
</ul>

<p>以整数形式返回满足题目要求的最长子数组的长度。</p>

<p><strong>注意：子数组</strong> 是数组中的一个连续非空元素序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [3,2,5,4], threshold = 5
<strong>输出：</strong>3
<strong>解释：</strong>在这个示例中，我们选择从 l = 1 开始、到 r = 3 结束的子数组 =&gt; [2,5,4] ，满足上述条件。
因此，答案就是这个子数组的长度 3 。可以证明 3 是满足题目要求的最大长度。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,2], threshold = 2
<strong>输出：</strong>1
<strong>解释：</strong>
在这个示例中，我们选择从 l = 1 开始、到 r = 1 结束的子数组 =&gt; [2] 。
该子数组满足上述全部条件。可以证明 1 是满足题目要求的最大长度。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [2,3,4,5], threshold = 4
<strong>输出：</strong>3
<strong>解释：</strong>
在这个示例中，我们选择从 l = 0 开始、到 r = 2 结束的子数组 =&gt; [2,3,4] 。 
该子数组满足上述全部条件。
因此，答案就是这个子数组的长度 3 。可以证明 3 是满足题目要求的最大长度。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100 </code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100 </code></li>
	<li><code>1 &lt;= threshold &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过双指针遍历数组，寻找符合条件的最长奇偶交替子数组。

2. **综合思路：**
   - **双指针法：** 使用两个指针 `l` 和 `r`，`l` 用于标记子数组的起始位置，`r` 用于扩展子数组的末尾。通过检查当前数是否满足奇偶交替和不超过阈值的条件来更新子数组长度。
   - **滑动窗口法：** 由于双指针法本质上是滑动窗口的应用，所有实现都可以归为滑动窗口法。

3. **全量伪代码：**
   ```plaintext
   初始化 cnt 为 0
   初始化 max_cnt 为 0
   初始化 l 为 0
   初始化 r 为 0

   当 l 小于数组长度时：
       如果 nums[l] 是偶数且小于等于阈值：
           将 r 设为 l + 1
           更新 max_cnt 为 max(max_cnt, 1)
           当 r 小于数组长度时：
               如果 nums[r] 与 nums[r-1] 奇偶性不同且小于等于阈值：
                   更新 cnt 为 r - l + 1 或 r - l
                   更新 max_cnt 为 max(cnt, max_cnt)
                   增加 r
               否则：
                   退出循环
           将 l 设为 r
       否则：
           增加 l
   返回 max_cnt
   ```

4. **复杂度：**
   - **时间复杂度：** $O(n)$，因为每个元素最多被访问两次。
   - **空间复杂度：** $O(1)$，因为只使用了常数个额外变量。