# 3484. 交换后字典序最小的字符串

**难度**: Easy | **标签**: `String` `Greedy`

## 题目描述

<p>给你一个仅由数字组成的字符串 <code>s</code>，在最多交换一次 <strong>相邻 </strong>且具有相同 <strong>奇偶性 </strong>的数字后，返回可以得到的<span data-keyword="lexicographically-smaller-string">字典序最小的字符串</span>。</p>

<p>如果两个数字都是奇数或都是偶数，则它们具有相同的奇偶性。例如，5 和 9、2 和 4 奇偶性相同，而 6 和 9 奇偶性不同。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "45320"</span></p>

<p><strong>输出：</strong> <span class="example-io">"43520"</span></p>

<p><strong>解释：</strong></p>

<p><code>s[1] == '5'</code> 和 <code>s[2] == '3'</code> 都具有相同的奇偶性，交换它们可以得到字典序最小的字符串。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "001"</span></p>

<p><strong>输出：</strong> <span class="example-io">"001"</span></p>

<p><strong>解释：</strong></p>

<p>无需进行交换，因为 <code>s</code> 已经是字典序最小的。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 仅由数字组成。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过一次相邻交换，确保相同奇偶性的相邻数字按升序排列，从而获得字典序最小的字符串。

2. 综合思路：
   - 迭代法：遍历字符串的每一对相邻字符，检查它们的奇偶性和大小关系，进行一次交换以获得字典序更小的字符串。

3. 全量伪代码：
   ```
   定义函数 getSmallestString，输入为字符串 s
       将字符串 s 转换为字符列表 nums
       从索引 1 开始遍历 nums 到末尾
           如果 nums[i-1] 和 nums[i] 的奇偶性相同
               如果 nums[i-1] 大于 nums[i]
                   交换 nums[i-1] 和 nums[i]
                   跳出循环
       将字符列表 nums 转换回字符串并返回
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度，因为最多需要遍历字符串一次。
   - 空间复杂度：$O(n)$，用于存储字符列表的空间。