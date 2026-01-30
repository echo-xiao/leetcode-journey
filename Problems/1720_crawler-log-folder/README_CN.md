# 1720. 文件夹操作日志搜集器

**难度**: Easy | **标签**: `Array` `String` `Stack`

## 题目描述

<p>每当用户执行变更文件夹操作时，LeetCode 文件系统都会保存一条日志记录。</p>

<p>下面给出对变更操作的说明：</p>

<ul>
	<li><code>&quot;../&quot;</code> ：移动到当前文件夹的父文件夹。如果已经在主文件夹下，则 <strong>继续停留在当前文件夹</strong> 。</li>
	<li><code>&quot;./&quot;</code> ：继续停留在当前文件夹<strong>。</strong></li>
	<li><code>&quot;x/&quot;</code> ：移动到名为 <code>x</code> 的子文件夹中。题目数据 <strong>保证总是存在文件夹 <code>x</code></strong> 。</li>
</ul>

<p>给你一个字符串列表 <code>logs</code> ，其中 <code>logs[i]</code> 是用户在 <code>i<sup>th</sup></code> 步执行的操作。</p>

<p>文件系统启动时位于主文件夹，然后执行 <code>logs</code> 中的操作。</p>

<p>执行完所有变更文件夹操作后，请你找出 <strong>返回主文件夹所需的最小步数</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/09/26/sample_11_1957.png" style="height: 151px; width: 775px;"></p>

<pre><strong>输入：</strong>logs = [&quot;d1/&quot;,&quot;d2/&quot;,&quot;../&quot;,&quot;d21/&quot;,&quot;./&quot;]
<strong>输出：</strong>2
<strong>解释：</strong>执行 &quot;../&quot; 操作变更文件夹 2 次，即可回到主文件夹
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/09/26/sample_22_1957.png" style="height: 270px; width: 600px;"></p>

<pre><strong>输入：</strong>logs = [&quot;d1/&quot;,&quot;d2/&quot;,&quot;./&quot;,&quot;d3/&quot;,&quot;../&quot;,&quot;d31/&quot;]
<strong>输出：</strong>3
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>logs = [&quot;d1/&quot;,&quot;../&quot;,&quot;../&quot;,&quot;../&quot;]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= logs.length &lt;= 10<sup>3</sup></code></li>
	<li><code>2 &lt;= logs[i].length &lt;= 10</code></li>
	<li><code>logs[i]</code> 包含小写英文字母，数字，<code>&#39;.&#39;</code> 和 <code>&#39;/&#39;</code></li>
	<li><code>logs[i]</code> 符合语句中描述的格式</li>
	<li>文件夹名称由小写英文字母和数字组成</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质**：使用栈模拟文件夹路径操作，最终栈的大小即为返回的结果。

2. **综合思路**：
   - **栈模拟法**：使用栈数据结构来模拟文件夹的进入和返回操作。对于每个日志指令，判断是进入子文件夹、返回上级文件夹还是保持当前文件夹，并对栈进行相应的操作。

3. **全量伪代码**：
   ```plaintext
   定义函数 minOperations，输入为日志列表 logs
       初始化空栈 stack
       对于 logs 中的每个指令 char
           如果指令是 "../"
               如果栈不为空
                   弹出栈顶元素
               否则
                   什么都不做
           否则如果指令是 "./"
               什么都不做
           否则
               将指令压入栈
       返回栈的长度
   ```

4. **复杂度**：
   - 时间复杂度：$O(n)$，其中 $n$ 是日志列表的长度，因为我们需要遍历每个日志指令。
   - 空间复杂度：$O(n)$，在最坏情况下，所有指令都是进入子文件夹的操作，栈的大小可能达到 $n$。