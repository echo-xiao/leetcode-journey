# 1537. 分割字符串的最大得分

**难度**: Easy | **标签**: `String` `Prefix Sum`

## 题目描述

<p>给你一个由若干 0 和 1 组成的字符串 <code>s</code> ，请你计算并返回将该字符串分割成两个 <strong>非空</strong> 子字符串（即&nbsp;<strong>左</strong> 子字符串和 <strong>右</strong> 子字符串）所能获得的最大得分。</p>

<p>「分割字符串的得分」为 <strong>左</strong> 子字符串中 <strong>0</strong> 的数量加上 <strong>右</strong> 子字符串中 <strong>1</strong> 的数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;011101&quot;
<strong>输出：</strong>5 
<strong>解释：</strong>
将字符串 s 划分为两个非空子字符串的可行方案有：
左子字符串 = &quot;0&quot; 且 右子字符串 = &quot;11101&quot;，得分 = 1 + 4 = 5 
左子字符串 = &quot;01&quot; 且 右子字符串 = &quot;1101&quot;，得分 = 1 + 3 = 4 
左子字符串 = &quot;011&quot; 且 右子字符串 = &quot;101&quot;，得分 = 1 + 2 = 3 
左子字符串 = &quot;0111&quot; 且 右子字符串 = &quot;01&quot;，得分 = 1 + 1 = 2 
左子字符串 = &quot;01110&quot; 且 右子字符串 = &quot;1&quot;，得分 = 2 + 1 = 3
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;00111&quot;
<strong>输出：</strong>5
<strong>解释：</strong>当 左子字符串 = &quot;00&quot; 且 右子字符串 = &quot;111&quot; 时，我们得到最大得分 = 2 + 3 = 5
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;1111&quot;
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 500</code></li>
	<li>字符串 <code>s</code> 仅由字符 <code>&#39;0&#39;</code> 和 <code>&#39;1&#39;</code> 组成。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过前缀和数组分别记录字符串中 '0' 和 '1' 的数量，计算每个可能的分割点的得分，并返回最大得分。

2. 综合思路：
   - 前缀和法：使用两个前缀和数组 `arr0` 和 `arr1` 分别记录从字符串开头到当前位置的 '0' 和 '1' 的累计数量，然后遍历每个可能的分割点，计算左侧 '0' 的数量加上右侧 '1' 的数量，找出最大值。
   - 目前提供的代码中只有一种解法，即前缀和法。

3. 全量伪代码：
   ```plaintext
   初始化 arr0 和 arr1 为长度为 len(s)+1 的数组，初始值为 0
   对于字符串 s 的每个字符 i：
       如果 s[i] 是 '0'：
           arr0[i+1] = arr0[i] + 1
           arr1[i+1] = arr1[i]
       如果 s[i] 是 '1'：
           arr0[i+1] = arr0[i]
           arr1[i+1] = arr1[i] + 1

   初始化 res 为一个空列表
   对于每个可能的分割点 i 从 1 到 len(s)-1：
       计算左侧 '0' 的数量 left = arr0[i]
       计算右侧 '1' 的数量 right = arr1[-1] - arr1[i]
       计算总得分 ttl = left + right
       将 ttl 添加到 res 中

   返回 res 中的最大值
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度，因为我们需要遍历字符串两次。
   - 空间复杂度：$O(n)$，因为我们使用了两个长度为 $n+1$ 的数组来存储前缀和。