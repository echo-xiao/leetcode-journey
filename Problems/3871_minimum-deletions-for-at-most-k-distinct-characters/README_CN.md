# 3871. 不同字符数量最多为 K 时的最少删除数

**难度**: Easy | **标签**: `Hash Table` `String` `Greedy` `Sorting` `Counting`

## 题目描述

<p>给你一个字符串 <code>s</code>（由小写英文字母组成）和一个整数 <code>k</code>。</p>

<p>你的任务是删除字符串中的一些字符（可以不删除任何字符），使得结果字符串中的&nbsp;<strong>不同字符数量&nbsp;</strong>最多为 <code>k</code>。</p>

<p>返回为达到上述目标所需删除的&nbsp;<strong>最小&nbsp;</strong>字符数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "abc", k = 2</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><code>s</code> 有三个不同的字符：<code>'a'</code>、<code>'b'</code> 和 <code>'c'</code>，每个字符的出现频率为 1。</li>
	<li>由于最多只能有 <code>k = 2</code> 个不同字符，需要删除某一个字符的所有出现。</li>
	<li>例如，删除所有 <code>'c'</code> 后，结果字符串中的不同字符数最多为 <code>k</code>。因此，答案是 1。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "aabb", k = 2</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><code>s</code> 有两个不同的字符（<code>'a'</code> 和 <code>'b'</code>），它们的出现频率分别为 2 和 2。</li>
	<li>由于最多可以有 <code>k = 2</code> 个不同字符，不需要删除任何字符。因此，答案是 0。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "yyyzz", k = 1</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><code>s</code> 有两个不同的字符（<code>'y'</code> 和 <code>'z'</code>），它们的出现频率分别为 3 和 2。</li>
	<li>由于最多只能有 <code>k = 1</code> 个不同字符，需要删除某一个字符的所有出现。</li>
	<li>删除所有 <code>'z'</code> 后，结果字符串中的不同字符数最多为 <code>k</code>。因此，答案是 2。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>1 &lt;= k &lt;= 16</code></li>
	<li><code>s</code> 仅由小写英文字母组成。</li>
</ul>

<p>&nbsp;</p>


---
## 解题思路与复盘

1. 一句话直击本质：通过统计字符频率并排序，删除频率最低的字符以确保不同字符数量不超过 K。

2. 综合思路：
   - 迭代法：遍历字符串统计每个字符的出现次数，存入字典中，然后将字典中的频率值提取出来排序，计算需要删除的字符数量。
   - 由于提供的代码版本逻辑完全相同，因此没有其他不同的解法。

3. 全量伪代码：
   ```
   定义函数 minDeletion(s, k)
       初始化空字典 dic
       对于字符串 s 中的每个字符 i
           如果 i 不在 dic 中
               将 i 添加到 dic 中，值为 1
           否则
               将 dic 中 i 的值加 1
       
       将 dic 中的所有值（即字符频率）存入列表 cnt
       对列表 cnt 进行排序
       
       计算 cnt 的长度 n
       计算需要保留的字符种类数 l = n - k
       
       如果 l 小于等于 0
           返回 0
       
       返回 cnt 中前 l 个元素的和（即需要删除的字符总数）
   ```

4. 复杂度：
   - 时间复杂度：$O(n + m \log m)$，其中 $n$ 是字符串的长度，用于统计字符频率，$m$ 是不同字符的数量，用于排序。
   - 空间复杂度：$O(m)$，用于存储字符频率的字典和频率列表。