# 2148. 使每位学生都有座位的最少移动次数

**难度**: Easy | **标签**: `Array` `Greedy` `Sorting` `Counting Sort`

## 题目描述

<p>一个房间里有 <code>n</code>&nbsp;个 <strong>空闲</strong> 座位和 <code>n</code>&nbsp;名 <strong>站着的</strong>&nbsp;学生，房间用一个数轴表示。给你一个长度为 <code>n</code>&nbsp;的数组&nbsp;<code>seats</code>&nbsp;，其中&nbsp;<code>seats[i]</code> 是第 <code>i</code>&nbsp;个座位的位置。同时给你一个长度为 <code>n</code>&nbsp;的数组&nbsp;<code>students</code>&nbsp;，其中&nbsp;<code>students[j]</code>&nbsp;是第 <code>j</code>&nbsp;位学生的位置。</p>

<p>你可以执行以下操作任意次：</p>

<ul>
	<li>增加或者减少第&nbsp;<code>i</code>&nbsp;位学生的位置，每次变化量为 <code>1</code>&nbsp;（也就是将第 <code>i</code>&nbsp;位学生从位置 <code>x</code>&nbsp;移动到 <code>x + 1</code>&nbsp;或者 <code>x - 1</code>）</li>
</ul>

<p>请你返回使所有学生都有座位坐的 <strong>最少移动次数</strong>&nbsp;，并确保没有两位学生的座位相同。</p>

<p>请注意，初始时有可能有多个座位或者多位学生在 <strong>同一</strong>&nbsp;位置。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>seats = [3,1,5], students = [2,7,4]
<b>输出：</b>4
<b>解释：</b>学生移动方式如下：
- 第一位学生从位置 2 移动到位置 1 ，移动 1 次。
- 第二位学生从位置 7 移动到位置 5 ，移动 2 次。
- 第三位学生从位置 4 移动到位置 3 ，移动 1 次。
总共 1 + 2 + 1 = 4 次移动。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>seats = [4,1,5,9], students = [1,3,2,6]
<b>输出：</b>7
<strong>解释：</strong>学生移动方式如下：
- 第一位学生不移动。
- 第二位学生从位置 3 移动到位置 4 ，移动 1 次。
- 第三位学生从位置 2 移动到位置 5 ，移动 3 次。
- 第四位学生从位置 6 移动到位置 9 ，移动 3 次。
总共 0 + 1 + 3 + 3 = 7 次移动。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>seats = [2,2,6,6], students = [1,3,2,6]
<b>输出：</b>4
<b>解释：</b>学生移动方式如下：
- 第一位学生从位置 1 移动到位置 2 ，移动 1 次。
- 第二位学生从位置 3 移动到位置 6 ，移动 3 次。
- 第三位学生不移动。
- 第四位学生不移动。
总共 1 + 3 + 0 + 0 = 4 次移动。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == seats.length == students.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= seats[i], students[j] &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过排序座位和学生位置后逐一匹配，计算每对座位和学生之间的距离之和来得到最小移动次数。

2. 综合思路：
   - 排序法：将座位和学生的位置分别排序，然后逐一匹配计算距离之和，这是最直接且高效的方法。
   - 其他可能的思路（未在提供的代码中出现）：可以考虑使用双指针法来优化某些特定情况下的匹配过程，但在本题中排序法已经是最优解。

3. 全量伪代码：
   ```
   定义函数 minMovesToSeat(seats, students):
       对 seats 进行升序排序
       对 students 进行升序排序
       初始化 res 为 0
       
       对于每个索引 i 从 0 到 seats 的长度减 1:
           计算 diff 为 seats[i] 和 students[i] 的绝对差值
           将 diff 加到 res 上
       
       返回 res
   ```

4. 复杂度：
   - 时间复杂度：$O(n \log n)$，其中 $n$ 是座位或学生的数量，因为排序操作是主要的时间消耗。
   - 空间复杂度：$O(1)$，如果不考虑输入输出的存储，排序操作是在原地进行的。