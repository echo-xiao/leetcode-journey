# 455. 分发饼干

**难度**: Easy | **标签**: `Array` `Two Pointers` `Greedy` `Sorting`

## 题目描述

<p>假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。</p>

<p>对每个孩子 <code>i</code>，都有一个胃口值&nbsp;<code>g[i]</code><sub>，</sub>这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 <code>j</code>，都有一个尺寸 <code>s[j]</code><sub>&nbsp;</sub>。如果 <code>s[j]&nbsp;&gt;= g[i]</code>，我们可以将这个饼干 <code>j</code> 分配给孩子 <code>i</code> ，这个孩子会得到满足。你的目标是满足尽可能多的孩子，并输出这个最大数值。</p>
&nbsp;

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> g = [1,2,3], s = [1,1]
<strong>输出:</strong> 1
<strong>解释:</strong> 
你有三个孩子和两块小饼干，3 个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是 1，你只能让胃口值是 1 的孩子满足。
所以你应该输出 1。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> g = [1,2], s = [1,2,3]
<strong>输出:</strong> 2
<strong>解释:</strong> 
你有两个孩子和三块小饼干，2 个孩子的胃口值分别是 1,2。
你拥有的饼干数量和尺寸都足以让所有孩子满足。
所以你应该输出 2。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= g.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= g[i], s[j] &lt;=&nbsp;2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与&nbsp;<a href="https://leetcode.cn/problems/maximum-matching-of-players-with-trainers/">2410. 运动员和训练师的最大匹配数</a>&nbsp;题相同。</p>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过排序和双指针遍历，尽可能用最小的饼干满足胃口最小的孩子。

2. **综合思路：**
   - **排序 + 双指针：** 所有版本都采用了这种方法。首先对孩子的胃口数组和饼干大小数组进行排序，然后使用两个指针分别遍历这两个数组，尝试用最小的饼干满足胃口最小的孩子。如果当前饼干能满足当前孩子，则两个指针都向前移动；否则，只移动饼干指针，直到找到能满足当前孩子的饼干。

3. **全量伪代码：**
   ```
   定义函数 findContentChildren(孩子胃口数组 g, 饼干大小数组 s):
       对 g 进行升序排序
       对 s 进行升序排序
       初始化满足孩子数量计数器 k 为 0
       初始化孩子指针 i 为 0
       初始化饼干指针 j 为 0

       当 i 小于 g 的长度 且 j 小于 s 的长度时:
           如果 s[j] >= g[i]:
               增加 k
               增加 i
               增加 j
           否则:
               增加 j

       返回 k
   ```

4. **复杂度：**
   - **时间复杂度：** $O(n \log n + m \log m)$，其中 $n$ 是孩子数组的长度，$m$ 是饼干数组的长度。排序操作的时间复杂度为 $O(n \log n)$ 和 $O(m \log m)$，遍历的时间复杂度为 $O(n + m)$。
   - **空间复杂度：** $O(1)$，除了输入和输出外，算法只使用了常数级别的额外空间。