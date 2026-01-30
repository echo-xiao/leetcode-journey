# 475. 供暖器

**难度**: Medium | **标签**: `Array` `Two Pointers` `Binary Search` `Sorting`

## 题目描述

<p>冬季已经来临。&nbsp;你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。</p>

<p>在加热器的加热半径范围内的每个房屋都可以获得供暖。</p>

<p>现在，给出位于一条水平线上的房屋&nbsp;<code>houses</code> 和供暖器&nbsp;<code>heaters</code> 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。</p>

<p><b>注意</b>：所有供暖器 <code>heaters</code> 都遵循你的半径标准，加热的半径也一样。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> houses = [1,2,3], heaters = [2]
<strong>输出:</strong> 1
<strong>解释:</strong> 仅在位置 2 上有一个供暖器。如果我们将加热半径设为 1，那么所有房屋就都能得到供暖。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> houses = [1,2,3,4], heaters = [1,4]
<strong>输出:</strong> 1
<strong>解释:</strong> 在位置 1, 4 上有两个供暖器。我们需要将加热半径设为 1，这样所有房屋就都能得到供暖。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>houses = [1,5], heaters = [2]
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= houses.length, heaters.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= houses[i], heaters[i] &lt;= 10<sup>9</sup></code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：**  
   使用二分查找找到每个房子最近的供暖器，然后计算所有房子到其最近供暖器的最大距离。

2. **综合思路：**  
   该问题的解决方案主要依赖于排序和二分查找。以下是详细思路：
   - **排序和二分查找：** 首先对供暖器的位置进行排序，然后对于每个房子，使用二分查找来找到其最近的左侧和右侧供暖器，计算到这两个供暖器的距离，选择较小的距离作为该房子的供暖距离。最后，所有房子的供暖距离中最大的值即为所需的最小供暖半径。
   - **线性扫描（未在提供的代码中实现）：** 另一种思路是先对房子和供暖器都排序，然后通过线性扫描同时遍历房子和供暖器，计算每个房子到最近供暖器的距离。这种方法可以避免二分查找的复杂性。

3. **全量伪代码：**  
   下面是基于排序和二分查找的伪代码：
   ```
   定义函数 findRadius(houses, heaters):
       将 heaters 排序
       初始化 dis 列表为空
       对于每个房子 h 在 houses 中:
           计算 h 到最近左侧供暖器的距离 leftDis = closestDistance(heaters, h, toLeft=True)
           计算 h 到最近右侧供暖器的距离 rightDis = closestDistance(heaters, h, toLeft=False)
           将 min(leftDis, rightDis) 添加到 dis 列表
       返回 dis 列表中的最大值

   定义函数 closestDistance(heaters, h, toLeft):
       初始化 left 为 0, right 为 heaters 的长度减 1
       当 left 小于等于 right 时:
           计算 mid 为 left 和 right 的中间索引
           如果 heaters[mid] 等于 h:
               返回 0
           否则如果 heaters[mid] 大于 h:
               将 right 更新为 mid - 1
           否则:
               将 left 更新为 mid + 1
       
       如果 toLeft 为 True:
           如果 right 小于 0:
               返回正无穷
           返回 h 减去 heaters[right]
       否则:
           如果 left 大于等于 heaters 的长度:
               返回正无穷
           返回 heaters[left] 减去 h
   ```

4. **复杂度：**  
   - **时间复杂度：** $O(n \log m)$，其中 $n$ 是房子的数量，$m$ 是供暖器的数量。排序供暖器需要 $O(m \log m)$，对每个房子进行二分查找需要 $O(\log m)$，总共需要 $O(n \log m)$。
   - **空间复杂度：** $O(1)$，除了输入和输出外，算法只使用了常数级别的额外空间。