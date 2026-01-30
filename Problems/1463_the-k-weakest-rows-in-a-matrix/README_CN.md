# 1463. 矩阵中战斗力最弱的 K 行

**难度**: Easy | **标签**: `Array` `Binary Search` `Sorting` `Heap (Priority Queue)` `Matrix`

## 题目描述

<p>给你一个大小为 <code>m * n</code> 的矩阵 <code>mat</code>，矩阵由若干军人和平民组成，分别用 1 和 0 表示。</p>

<p>请你返回矩阵中战斗力最弱的 <code>k</code> 行的索引，按从最弱到最强排序。</p>

<p>如果第 <em><strong>i</strong></em> 行的军人数量少于第 <em><strong>j</strong></em> 行，或者两行军人数量相同但<em><strong> i</strong></em> 小于 <em><strong>j</strong></em>，那么我们认为第<em><strong> i </strong></em>行的战斗力比第<em><strong> j </strong></em>行弱。</p>

<p>军人 <strong>总是</strong> 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
<strong>输出：</strong>[2,0,3]
<strong>解释：</strong>
每行中的军人数目：
行 0 -> 2 
行 1 -> 4 
行 2 -> 1 
行 3 -> 2 
行 4 -> 5 
从最弱到最强对这些行排序后得到 [2,0,3,1,4]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
<strong>输出：</strong>[0,2]
<strong>解释：</strong> 
每行中的军人数目：
行 0 -> 1 
行 1 -> 4 
行 2 -> 1 
行 3 -> 1 
从最弱到最强对这些行排序后得到 [0,2,3,1]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>2 <= n, m <= 100</code></li>
	<li><code>1 <= k <= m</code></li>
	<li><code>matrix[i][j]</code> 不是 0 就是 1</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：用一句话总结该算法的核心逻辑。**

   - 通过计算每行的战斗力（即1的数量），然后使用排序或堆结构找出战斗力最弱的K行。

2. **综合思路：**

   - **堆结构解法：** 使用最大堆来维护最弱的K行，通过将每行的战斗力和行索引作为元素插入堆中，确保堆的大小不超过K，从而在遍历完成后得到最弱的K行。
   
   - **二分查找与排序解法：** 对每行使用二分查找来计算战斗力（即1的数量），然后将战斗力和行索引存储在列表中，最后对列表进行排序并选择前K个元素。

3. **全量伪代码：**

   - **堆结构解法伪代码：**
     ```
     初始化最大堆 maxHeap
     对于每一行 idx 从 0 到 mat 的长度：
         计算该行的战斗力 cnt（即1的数量）
         创建元素 item = [-cnt, -idx]
         如果 maxHeap 的大小小于 k：
             将 item 插入 maxHeap
         否则：
             将 item 插入 maxHeap 并弹出最大元素
     初始化结果列表 res
     当 maxHeap 不为空：
         弹出 maxHeap 的元素 cnt, idx
         将 -idx 添加到 res
     返回 res 的逆序
     ```

   - **二分查找与排序解法伪代码：**
     ```
     初始化列表 dis
     对于每一行 i 从 0 到 mat 的长度：
         获取该行 lst
         如果 lst 的第一个元素为 0：
             将 (0, i) 添加到 dis
             继续下一行
         初始化 left = 0, right = lst 的长度 - 1
         初始化 first = 0, last = 0
         当 left <= right：
             计算 mid = left + (right - left) // 2
             如果 lst[mid] == 1：
                 last = mid
                 left = mid + 1
             否则：
                 right = mid - 1
         将 (last - first + 1, i) 添加到 dis
     对 dis 进行排序
     初始化结果列表 res
     对于前 k 个元素：
         将元素的索引添加到 res
     返回 res
     ```

4. **复杂度：**

   - **堆结构解法：**
     - 时间复杂度：$O(n \log k)$，其中 $n$ 是矩阵的行数，因为每次插入堆的操作复杂度为 $O(\log k)$。
     - 空间复杂度：$O(k)$，用于存储堆中的元素。

   - **二分查找与排序解法：**
     - 时间复杂度：$O(n \log m + n \log n)$，其中 $m$ 是矩阵的列数，$n$ 是矩阵的行数。二分查找每行的复杂度为 $O(\log m)$，排序的复杂度为 $O(n \log n)$。
     - 空间复杂度：$O(n)$，用于存储每行的战斗力和索引。