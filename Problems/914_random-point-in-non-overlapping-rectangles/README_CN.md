# 914. 非重叠矩形中的随机点

**难度**: Medium | **标签**: `Array` `Math` `Binary Search` `Reservoir Sampling` `Prefix Sum` `Ordered Set` `Randomized`

## 题目描述

<p>给定一个由非重叠的轴对齐矩形的数组 <code>rects</code> ，其中 <code>rects[i] = [ai, bi, xi, yi]</code> 表示 <code>(ai, bi)</code> 是第 <code>i</code> 个矩形的左下角点，<code>(xi, yi)</code> 是第 <code>i</code> 个矩形的右上角点。设计一个算法来随机挑选一个被某一矩形覆盖的整数点。矩形周长上的点也算做是被矩形覆盖。所有满足要求的点必须等概率被返回。</p>

<p>在给定的矩形覆盖的空间内的任何整数点都有可能被返回。</p>

<p><strong>请注意&nbsp;</strong>，整数点是具有整数坐标的点。</p>

<p>实现&nbsp;<code>Solution</code>&nbsp;类:</p>

<ul>
	<li><code>Solution(int[][] rects)</code>&nbsp;用给定的矩形数组&nbsp;<code>rects</code> 初始化对象。</li>
	<li><code>int[] pick()</code>&nbsp;返回一个随机的整数点 <code>[u, v]</code> 在给定的矩形所覆盖的空间内。</li>
</ul>

<ol>
</ol>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/07/24/lc-pickrandomrec.jpg" style="height: 539px; width: 419px;" /></p>

<pre>
<strong>输入: 
</strong>["Solution", "pick", "pick", "pick", "pick", "pick"]
[[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
<strong>输出: 
</strong>[null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]

<strong>解释：</strong>
Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
solution.pick(); // 返回 [1, -2]
solution.pick(); // 返回 [1, -1]
solution.pick(); // 返回 [-1, -2]
solution.pick(); // 返回 [-2, -2]
solution.pick(); // 返回 [0, 0]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= rects.length &lt;= 100</code></li>
	<li><code>rects[i].length == 4</code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= a<sub>i</sub>&nbsp;&lt; x<sub>i</sub>&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= b<sub>i</sub>&nbsp;&lt; y<sub>i</sub>&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>x<sub>i</sub>&nbsp;- a<sub>i</sub>&nbsp;&lt;= 2000</code></li>
	<li><code>y<sub>i</sub>&nbsp;- b<sub>i</sub>&nbsp;&lt;= 2000</code></li>
	<li>所有的矩形不重叠。</li>
	<li><code>pick</code> 最多被调用&nbsp;<code>10<sup>4</sup></code>&nbsp;次。</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过前缀和数组和二分查找，按面积比例随机选择一个矩形，然后在该矩形内随机选择一个点。

2. **综合思路：**
   - **前缀和与二分查找：** 计算每个矩形的面积并构建前缀和数组，用于快速确定随机点属于哪个矩形。通过随机数生成器和二分查找，按面积比例选择矩形。
   - **随机点选择：** 在选定的矩形内，通过随机数生成器选择一个具体的点。

3. **全量伪代码：**

   ```plaintext
   初始化函数(rects):
       存储矩形列表为 rects
       初始化前缀和数组 prefixSum 为 []
       初始化总面积 ttl 为 0

       对于每个矩形 (a, b, x, y) 在 rects 中:
           计算矩形的点数 cnt = (x - a + 1) * (y - b + 1)
           更新总面积 ttl += cnt
           将当前总面积 ttl 添加到 prefixSum

   随机选择函数 pick():
       生成一个随机整数 target 在 1 到 ttl 之间
       使用二分查找在 prefixSum 中找到 target 所对应的矩形索引 idx
       获取矩形的坐标 (a, b, x, y) = rects[idx]
       在矩形内随机选择一个点 pickX = 随机整数在 a 到 x 之间
       在矩形内随机选择一个点 pickY = 随机整数在 b 到 y 之间
       返回点 [pickX, pickY]
   ```

4. **复杂度：**

   - 时间复杂度：初始化时为 $O(n)$，其中 $n$ 是矩形的数量；每次调用 `pick` 方法的时间复杂度为 $O(\log n)$，因为使用了二分查找。
   - 空间复杂度：$O(n)$，用于存储前缀和数组。