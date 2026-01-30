# 789. 数据流中的第 K 大元素

**难度**: Easy | **标签**: `Tree` `Design` `Binary Search Tree` `Heap (Priority Queue)` `Binary Tree` `Data Stream`

## 题目描述

<p>设计一个找到数据流中第 <code>k</code> 大元素的类（class）。注意是排序后的第 <code>k</code> 大元素，不是第 <code>k</code> 个不同的元素。</p>

<p>请实现 <code>KthLargest</code>&nbsp;类：</p>

<ul>
	<li><code>KthLargest(int k, int[] nums)</code> 使用整数 <code>k</code> 和整数流 <code>nums</code> 初始化对象。</li>
	<li><code>int add(int val)</code> 将 <code>val</code> 插入数据流 <code>nums</code> 后，返回当前数据流中第 <code>k</code> 大的元素。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><br />
<span class="example-io">["KthLargest", "add", "add", "add", "add", "add"]<br />
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]</span></p>

<p><strong>输出：</strong><span class="example-io">[null, 4, 5, 5, 8, 8]</span></p>

<p><strong>解释：</strong></p>

<p>KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);<br />
kthLargest.add(3); // 返回 4<br />
kthLargest.add(5); // 返回 5<br />
kthLargest.add(10); // 返回 5<br />
kthLargest.add(9); // 返回 8<br />
kthLargest.add(4); // 返回 8</p>

<p>&nbsp;</p>
</div>

<p><strong class="example">示例&nbsp;2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><br />
<span class="example-io">["KthLargest", "add", "add", "add", "add"]<br />
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]</span></p>

<p><span class="example-io"><b>输出：</b>[null, 7, 7, 7, 8]</span></p>

<p><strong>解释：</strong></p>
KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);<br />
kthLargest.add(2); // 返回 7<br />
kthLargest.add(10); // 返回 7<br />
kthLargest.add(9); // 返回 7<br />
kthLargest.add(9); // 返回 8</div>

<p>&nbsp;</p>
<strong>提示：</strong>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length + 1</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= val &lt;= 10<sup>4</sup></code></li>
	<li>最多调用 <code>add</code> 方法 <code>10<sup>4</sup></code> 次</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：
   - 使用最小堆维护数据流中的前 K 大元素，堆顶即为第 K 大元素。

2. 综合思路：
   - 所有版本都采用了最小堆的数据结构来解决问题，核心思路是通过维护一个大小为 K 的最小堆来动态获取数据流中的第 K 大元素。
   - 版本 1 和 2 的实现逻辑完全相同，都是在初始化时逐个添加元素到堆中，并在添加新元素时根据堆的大小和堆顶元素进行调整。
   - 版本 3 在初始化时直接对输入数组进行堆化，并通过弹出多余元素来确保堆的大小不超过 K。

3. 全量伪代码：
   - 初始化：
     ```
     初始化最小堆 minHeap
     设置 k 为第 K 大元素的目标位置
     对于输入数组 nums 中的每个元素 num：
         调用 add(num)
     ```
   - 添加元素：
     ```
     函数 add(val):
         如果 minHeap 的大小小于 k：
             将 val 推入 minHeap
         否则如果 val 大于 minHeap 的堆顶元素：
             用 val 替换 minHeap 的堆顶元素
         返回 minHeap 的堆顶元素
     ```
   - 版本 3 的初始化：
     ```
     对 nums 进行堆化
     当 nums 的大小大于 k 时：
         弹出 nums 的堆顶元素
     ```

4. 复杂度：
   - 时间复杂度：初始化时为 $O(n \log k)$，每次添加元素为 $O(\log k)$，其中 $n$ 是初始数组的大小。
   - 空间复杂度：$O(k)$，用于存储最小堆中的 K 个元素。