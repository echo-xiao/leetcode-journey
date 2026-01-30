# 93. 复原 IP 地址

**难度**: Medium | **标签**: `String` `Backtracking`

## 题目描述

<p><strong>有效 IP 地址</strong> 正好由四个整数（每个整数位于 <code>0</code> 到 <code>255</code> 之间组成，且不能含有前导 <code>0</code>），整数之间用 <code>'.'</code> 分隔。</p>

<ul>
	<li>例如：<code>"0.1.2.201"</code> 和<code> "192.168.1.1"</code> 是 <strong>有效</strong> IP 地址，但是 <code>"0.011.255.245"</code>、<code>"192.168.1.312"</code> 和 <code>"192.168@1.1"</code> 是 <strong>无效</strong> IP 地址。</li>
</ul>

<p>给定一个只包含数字的字符串 <code>s</code> ，用以表示一个 IP 地址，返回所有可能的<strong>有效 IP 地址</strong>，这些地址可以通过在 <code>s</code> 中插入&nbsp;<code>'.'</code> 来形成。你 <strong>不能</strong>&nbsp;重新排序或删除 <code>s</code> 中的任何数字。你可以按 <strong>任何</strong> 顺序返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "25525511135"
<strong>输出：</strong>["255.255.11.135","255.255.111.35"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "0000"
<strong>输出：</strong>["0.0.0.0"]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "101023"
<strong>输出：</strong>["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 20</code></li>
	<li><code>s</code> 仅由数字组成</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用深度优先搜索（DFS）递归地尝试所有可能的分段组合，确保每段合法以复原 IP 地址。

2. 综合思路：
   - **递归 + DFS**：所有版本均采用递归的深度优先搜索方法，逐步构建可能的 IP 地址分段，确保每个分段的合法性（长度、数值范围、前导零）。
   - **剪枝优化**：在递归过程中，通过计算剩余字符数与剩余分段数的关系，提前剪枝不可能的路径。

3. 全量伪代码：
   ```
   定义函数 restoreIpAddresses(s: 字符串) -> 列表:
       初始化结果列表 res
       调用 dfs(s, 0, 空列表, res)
       返回 res

   定义函数 dfs(s: 字符串, start: 整数, path: 列表, res: 列表):
       如果 path 长度为 4:
           如果 start 等于 s 的长度:
               将 path 拼接成 IP 地址格式并加入 res
           返回

       计算剩余分段数 rem = 4 - path 的长度
       如果 s 的剩余长度大于 rem * 3 或小于 rem:
           返回

       对于 size 从 1 到 3:
           如果 start + size 超过 s 的长度:
               退出循环

           取出子串 segment = s[start: start + size]

           如果 segment 长度大于 1 且 segment 的第一个字符为 '0' 或 segment 转换为整数大于 255:
               跳过当前循环

           将 segment 加入 path
           递归调用 dfs(s, start + size, path, res)
           从 path 移除最后一个元素
   ```

4. 复杂度：
   - 时间复杂度：$O(3^4)$，因为最多有 4 段，每段最多有 3 种选择。
   - 空间复杂度：$O(4)$，递归深度最多为 4，存储路径的空间。