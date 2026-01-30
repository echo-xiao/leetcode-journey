# 2551. 对数组执行操作

**难度**: Easy | **标签**: `Array` `Two Pointers` `Simulation`

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的数组 <code>nums</code> ，数组大小为 <code>n</code> ，且由 <strong>非负</strong> 整数组成。</p>

<p>你需要对数组执行 <code>n - 1</code> 步操作，其中第 <code>i</code> 步操作（从 <strong>0</strong> 开始计数）要求对 <code>nums</code> 中第 <code>i</code> 个元素执行下述指令：</p>

<ul>
	<li>如果 <code>nums[i] == nums[i + 1]</code> ，则 <code>nums[i]</code> 的值变成原来的 <code>2</code> 倍，<code>nums[i + 1]</code> 的值变成 <code>0</code> 。否则，跳过这步操作。</li>
</ul>

<p>在执行完 <strong>全部</strong> 操作后，将所有 <code>0</code> <strong>移动</strong> 到数组的 <strong>末尾</strong> 。</p>

<ul>
	<li>例如，数组 <code>[1,0,2,0,0,1]</code> 将所有 <code>0</code> 移动到末尾后变为 <code>[1,2,1,0,0,0]</code> 。</li>
</ul>

<p>返回结果数组。</p>

<p><strong>注意</strong> 操作应当 <strong>依次有序</strong> 执行，而不是一次性全部执行。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,2,1,1,0]
<strong>输出：</strong>[1,4,2,0,0,0]
<strong>解释：</strong>执行以下操作：
- i = 0: nums[0] 和 nums[1] 不相等，跳过这步操作。
- i = 1: nums[1] 和 nums[2] 相等，nums[1] 的值变成原来的 2 倍，nums[2] 的值变成 0 。数组变成 [1,<em><strong>4</strong></em>,<em><strong>0</strong></em>,1,1,0] 。
- i = 2: nums[2] 和 nums[3] 不相等，所以跳过这步操作。
- i = 3: nums[3] 和 nums[4] 相等，nums[3] 的值变成原来的 2 倍，nums[4] 的值变成 0 。数组变成 [1,4,0,<em><strong>2</strong></em>,<em><strong>0</strong></em>,0] 。
- i = 4: nums[4] 和 nums[5] 相等，nums[4] 的值变成原来的 2 倍，nums[5] 的值变成 0 。数组变成 [1,4,0,2,<em><strong>0</strong></em>,<em><strong>0</strong></em>] 。
执行完所有操作后，将 0 全部移动到数组末尾，得到结果数组 [1,4,2,0,0,0] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1]
<strong>输出：</strong>[1,0]
<strong>解释：</strong>无法执行任何操作，只需要将 0 移动到末尾。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 2000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过合并相邻相等元素并将其后置为零，然后将所有非零元素移动到数组前面。

2. 综合思路：
   - **迭代法**：所有版本都采用了迭代法，通过遍历数组来合并相邻相等的元素，然后使用双指针或直接构建新数组的方式将非零元素移动到前面。
   - **双指针法**：版本 1 和 2 使用双指针法（快慢指针）来实现非零元素的移动。
   - **新数组法**：版本 3 通过构建一个新的结果数组来收集非零元素，再补充零。

3. 全量伪代码：
   - 初始化结果数组 `res` 和指针 `j` 为 0。
   - 遍历数组 `nums`，对于每个元素 `nums[i]`：
     - 如果 `nums[i]` 等于 `nums[i+1]`，则将 `nums[i]` 翻倍并将 `nums[i+1]` 置为 0。
   - 使用双指针法：
     - 初始化 `fast` 和 `slow` 指针为 0。
     - 当 `fast` 小于数组长度时：
       - 如果 `nums[fast]` 不为 0，交换 `nums[fast]` 和 `nums[slow]`，并将 `slow` 增加 1。
       - 将 `fast` 增加 1。
   - 使用新数组法：
     - 遍历 `nums`，将所有非零元素添加到 `res`。
     - 计算零的数量 `zeros` 为 `len(nums) - len(res)`。
     - 将 `zeros` 个零添加到 `res` 的末尾。
   - 返回结果数组 `res`。

4. 复杂度：
   - 时间复杂度：$O(n)$，因为每个元素最多被处理两次。
   - 空间复杂度：$O(n)$，版本 3 由于使用了额外的结果数组。版本 1 和 2 的空间复杂度为 $O(1)$，因为它们在原地修改数组。