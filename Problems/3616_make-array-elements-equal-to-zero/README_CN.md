# 3616. 使数组元素等于零

**难度**: Easy | **标签**: `Array` `Simulation` `Prefix Sum`

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code> 。</p>

<p>开始时，选择一个满足 <code>nums[curr] == 0</code> 的起始位置&nbsp;<code>curr</code>&nbsp;，并选择一个移动 <strong>方向</strong>&nbsp;：向左或者向右。</p>

<p>此后，你需要重复下面的过程：</p>

<ul>
	<li>如果&nbsp;<code>curr</code>&nbsp;超过范围&nbsp;<code>[0, n - 1]</code> ，过程结束。</li>
	<li>如果&nbsp;<code>nums[curr] == 0</code> ，沿当前方向继续移动：如果向右移，则 <strong>递增</strong>&nbsp;<code>curr</code>&nbsp;；如果向左移，则 <strong>递减</strong>&nbsp;<code>curr</code>&nbsp;。</li>
	<li>如果&nbsp;<code>nums[curr] &gt; 0</code>:
	<ul>
		<li>将&nbsp;<code>nums[curr]</code>&nbsp;减&nbsp;1 。</li>
		<li><strong>反转</strong>&nbsp;移动方向（向左变向右，反之亦然）。</li>
		<li>沿新方向移动一步。</li>
	</ul>
	</li>
</ul>

<p>如果在结束整个过程后，<code>nums</code>&nbsp;中的所有元素都变为 0 ，则认为选出的初始位置和移动方向 <strong>有效</strong>&nbsp;。</p>

<p>返回可能的有效选择方案数目。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,0,2,0,3]</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><b>解释：</b></p>

<p>可能的有效选择方案如下：</p>

<ul>
	<li>选择&nbsp;<code>curr = 3</code>&nbsp;并向左移动。

	<ul>
		<li><code>[1,0,2,<strong><u>0</u></strong>,3] -&gt; [1,0,<strong><u>2</u></strong>,0,3] -&gt; [1,0,1,<strong><u>0</u></strong>,3] -&gt; [1,0,1,0,<strong><u>3</u></strong>] -&gt; [1,0,1,<strong><u>0</u></strong>,2] -&gt; [1,0,<strong><u>1</u></strong>,0,2] -&gt; [1,0,0,<strong><u>0</u></strong>,2] -&gt; [1,0,0,0,<strong><u>2</u></strong>] -&gt; [1,0,0,<strong><u>0</u></strong>,1] -&gt; [1,0,<strong><u>0</u></strong>,0,1] -&gt; [1,<strong><u>0</u></strong>,0,0,1] -&gt; [<strong><u>1</u></strong>,0,0,0,1] -&gt; [0,<strong><u>0</u></strong>,0,0,1] -&gt; [0,0,<strong><u>0</u></strong>,0,1] -&gt; [0,0,0,<strong><u>0</u></strong>,1] -&gt; [0,0,0,0,<strong><u>1</u></strong>] -&gt; [0,0,0,0,0]</code>.</li>
	</ul>
	</li>
	<li>选择&nbsp;<code>curr = 3</code>&nbsp;并向右移动。
	<ul>
		<li><code>[1,0,2,<strong><u>0</u></strong>,3] -&gt; [1,0,2,0,<strong><u>3</u></strong>] -&gt; [1,0,2,<strong><u>0</u></strong>,2] -&gt; [1,0,<strong><u>2</u></strong>,0,2] -&gt; [1,0,1,<strong><u>0</u></strong>,2] -&gt; [1,0,1,0,<strong><u>2</u></strong>] -&gt; [1,0,1,<strong><u>0</u></strong>,1] -&gt; [1,0,<strong><u>1</u></strong>,0,1] -&gt; [1,0,0,<strong><u>0</u></strong>,1] -&gt; [1,0,0,0,<strong><u>1</u></strong>] -&gt; [1,0,0,<strong><u>0</u></strong>,0] -&gt; [1,0,<strong><u>0</u></strong>,0,0] -&gt; [1,<strong><u>0</u></strong>,0,0,0] -&gt; [<strong><u>1</u></strong>,0,0,0,0] -&gt; [0,0,0,0,0].</code></li>
	</ul>
	</li>
</ul>
</div>

<p><b>示例 2：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2,3,4,0,4,1,0]</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><b>解释：</b></p>

<p>不存在有效的选择方案。</p>
</div>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
	<li>至少存在一个元素&nbsp;<code>i</code>&nbsp;满足&nbsp;<code>nums[i] == 0</code> 。</li>
</ul>


---
## 解题思路与复盘

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