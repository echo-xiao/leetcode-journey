# 1802. 无法吃午餐的学生数量

**难度**: Easy | **标签**: `Array` `Stack` `Queue` `Simulation`

## 题目描述

<p>学校的自助午餐提供圆形和方形的三明治，分别用数字 <code>0</code> 和 <code>1</code> 表示。所有学生站在一个队列里，每个学生要么喜欢圆形的要么喜欢方形的。<br>
餐厅里三明治的数量与学生的数量相同。所有三明治都放在一个 <strong>栈</strong> 里，每一轮：</p>

<ul>
	<li>如果队列最前面的学生 <strong>喜欢</strong> 栈顶的三明治，那么会 <strong>拿走它</strong> 并离开队列。</li>
	<li>否则，这名学生会 <strong>放弃这个三明治</strong> 并回到队列的尾部。</li>
</ul>

<p>这个过程会一直持续到队列里所有学生都不喜欢栈顶的三明治为止。</p>

<p>给你两个整数数组 <code>students</code> 和 <code>sandwiches</code> ，其中 <code>sandwiches[i]</code> 是栈里面第 <code>i<sup>​​​​​​</sup></code> 个三明治的类型（<code>i = 0</code> 是栈的顶部）， <code>students[j]</code> 是初始队列里第 <code>j<sup>​​​​​​</sup></code> 名学生对三明治的喜好（<code>j = 0</code> 是队列的最开始位置）。请你返回无法吃午餐的学生数量。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>students = [1,1,0,0], sandwiches = [0,1,0,1]
<b>输出：</b>0<strong> 
解释：</strong>
- 最前面的学生放弃最顶上的三明治，并回到队列的末尾，学生队列变为 students = [1,0,0,1]。
- 最前面的学生放弃最顶上的三明治，并回到队列的末尾，学生队列变为 students = [0,0,1,1]。
- 最前面的学生拿走最顶上的三明治，剩余学生队列为 students = [0,1,1]，三明治栈为 sandwiches = [1,0,1]。
- 最前面的学生放弃最顶上的三明治，并回到队列的末尾，学生队列变为 students = [1,1,0]。
- 最前面的学生拿走最顶上的三明治，剩余学生队列为 students = [1,0]，三明治栈为 sandwiches = [0,1]。
- 最前面的学生放弃最顶上的三明治，并回到队列的末尾，学生队列变为 students = [0,1]。
- 最前面的学生拿走最顶上的三明治，剩余学生队列为 students = [1]，三明治栈为 sandwiches = [1]。
- 最前面的学生拿走最顶上的三明治，剩余学生队列为 students = []，三明治栈为 sandwiches = []。
所以所有学生都有三明治吃。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
<b>输出：</b>3
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= students.length, sandwiches.length &lt;= 100</code></li>
	<li><code>students.length == sandwiches.length</code></li>
	<li><code>sandwiches[i]</code> 要么是 <code>0</code> ，要么是 <code>1</code> 。</li>
	<li><code>students[i]</code> 要么是 <code>0</code> ，要么是 <code>1</code> 。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用队列模拟学生排队和三明治的分发过程，通过记录尝试次数来判断是否无法再匹配。

2. 综合思路：
   - 迭代法：使用双端队列（deque）来模拟学生和三明治的队列，循环处理每个学生与当前三明治的匹配情况。
   - 逻辑上，两种实现方式是相同的，都是通过循环和条件判断来处理队列中的元素。

3. 全量伪代码：
   ```
   初始化学生队列和三明治堆栈为双端队列
   初始化尝试次数为0

   当学生队列和三明治堆栈都不为空时：
       如果尝试次数等于学生队列长度：
           跳出循环（无法再匹配）

       如果学生队列的第一个学生喜欢当前三明治：
           移除学生队列的第一个学生
           移除三明治堆栈的第一个三明治
           尝试次数重置为0
       否则：
           将学生队列的第一个学生移到队尾
           尝试次数加1

   返回学生队列的长度（即无法吃午餐的学生数量）
   ```

4. 复杂度：
   - 时间复杂度：$O(n^2)$，其中 $n$ 是学生的数量。在最坏情况下，每个学生可能需要被循环移动到队尾 $n$ 次。
   - 空间复杂度：$O(n)$，用于存储学生和三明治的队列。