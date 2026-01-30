# 2232. 向字符串添加空格

**难度**: Medium | **标签**: `Array` `Two Pointers` `String` `Simulation`

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的字符串 <code>s</code> ，以及一个下标从 <strong>0</strong> 开始的整数数组 <code>spaces</code> 。</p>

<p>数组 <code>spaces</code> 描述原字符串中需要添加空格的下标。每个空格都应该插入到给定索引处的字符值 <strong>之前</strong> 。</p>

<ul>
	<li>例如，<code>s = "EnjoyYourCoffee"</code> 且 <code>spaces = [5, 9]</code> ，那么我们需要在 <code>'Y'</code> 和 <code>'C'</code> 之前添加空格，这两个字符分别位于下标 <code>5</code> 和下标 <code>9</code> 。因此，最终得到 <code>"Enjoy <em><strong>Y</strong></em>our <em><strong>C</strong></em>offee"</code> 。</li>
</ul>

<p>请你添加空格，并返回修改后的字符串<em>。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
<strong>输出：</strong>"Leetcode Helps Me Learn"
<strong>解释：</strong>
下标 8、13 和 15 对应 "Leetcode<em><strong>H</strong></em>elps<em><strong>M</strong></em>e<em><strong>L</strong></em>earn" 中加粗斜体字符。
接着在这些字符前添加空格。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "icodeinpython", spaces = [1,5,7,9]
<strong>输出：</strong>"i code in py thon"
<strong>解释：</strong>
下标 1、5、7 和 9 对应 "i<em><strong>c</strong></em>ode<em><strong>i</strong></em>n<em><strong>p</strong></em>y<em><strong>t</strong></em>hon" 中加粗斜体字符。
接着在这些字符前添加空格。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "spacing", spaces = [0,1,2,3,4,5,6]
<strong>输出：</strong>" s p a c i n g"
<strong>解释：</strong>
字符串的第一个字符前可以添加空格。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> 仅由大小写英文字母组成</li>
	<li><code>1 &lt;= spaces.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>0 &lt;= spaces[i] &lt;= s.length - 1</code></li>
	<li><code>spaces</code> 中的所有值 <strong>严格递增</strong></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过从后向前遍历字符串和空格索引数组，逐个将字符和空格插入结果数组中，以避免在字符串中直接插入空格导致的复杂度增加。

2. **综合思路：**
   - **迭代法：** 所有版本都采用了迭代法，从字符串的末尾开始向前遍历，同时检查空格索引数组，决定在何处插入空格。这种方法避免了在字符串中直接插入空格的高复杂度操作。
   - **数据结构：** 使用一个结果数组 `res` 来存储最终的字符串，避免了在原字符串中插入空格的复杂度。

3. **全量伪代码：**
   ```plaintext
   定义函数 addSpaces(s, spaces):
       计算字符串 s 的长度 n1
       计算空格索引数组 spaces 的长度 n2
       计算结果字符串的总长度 n = n1 + n2
       初始化指针 i, j, k 分别指向 s 的末尾, spaces 的末尾, 结果数组的末尾
       初始化结果数组 res 长度为 n，所有元素为空字符串

       当 i >= 0 或 j >= 0 时，重复以下步骤:
           将 s[i] 赋值给 res[k]
           将 k 减 1
           如果 j >= 0 且 i 等于 spaces[j]:
               将空格赋值给 res[k]
               将 j 减 1
               将 k 减 1
           将 i 减 1

       返回通过连接 res 中所有元素得到的字符串
   ```

4. **复杂度：**
   - **时间复杂度：** $O(n)$，其中 $n$ 是字符串 $s$ 的长度，因为每个字符和空格索引都被遍历一次。
   - **空间复杂度：** $O(n)$，因为需要额外的数组来存储结果字符串。