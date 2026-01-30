# 1039. 找到小镇的法官

**难度**: Easy | **标签**: `Array` `Hash Table` `Graph Theory`

## 题目描述

<p>小镇里有 <code>n</code> 个人，按从 <code>1</code> 到 <code>n</code> 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。</p>

<p>如果小镇法官真的存在，那么：</p>

<ol>
	<li>小镇法官不会信任任何人。</li>
	<li>每个人（除了小镇法官）都信任这位小镇法官。</li>
	<li>只有一个人同时满足属性 <strong>1</strong> 和属性 <strong>2</strong> 。</li>
</ol>

<p>给你一个数组 <code>trust</code> ，其中 <code>trust[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示编号为 <code>a<sub>i</sub></code> 的人信任编号为 <code>b<sub>i</sub></code> 的人。</p>

<p>如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2, trust = [[1,2]]
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3, trust = [[1,3],[2,3]]
<strong>输出：</strong>3
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 3, trust = [[1,3],[2,3],[3,1]]
<strong>输出：</strong>-1
</pre>
&nbsp;

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= trust.length &lt;= 10<sup>4</sup></code></li>
	<li><code>trust[i].length == 2</code></li>
	<li><code>trust</code> 中的所有<code>trust[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> <strong>互不相同</strong></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>1 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：算法通过计算每个人的信任入度和出度，寻找唯一一个入度为 $n-1$ 且出度为 0 的人作为小镇的法官。

2. 综合思路：
   - 迭代法：使用两个数组分别记录每个人的信任入度和出度，遍历信任关系更新这两个数组，然后再遍历所有人，寻找符合条件的法官。
   - 该题目主要采用迭代法，没有递归、DFS、BFS等其他解法。

3. 全量伪代码：
   ```
   输入：n（小镇人数），trust（信任关系列表）
   初始化：indegree数组大小为n+1，全部元素设为0
          outdegree数组大小为n+1，全部元素设为0

   对于信任关系中的每对(u, v)：
       增加v的indegree
       增加u的outdegree

   对于每个人i从1到n：
       如果indegree[i]等于n-1且outdegree[i]等于0：
           返回i（i是法官）

   如果没有找到符合条件的人：
       返回-1（没有法官）
   ```

4. 复杂度：
   - 时间复杂度：$O(n + m)$，其中 $n$ 是小镇的人数，$m$ 是信任关系的数量，因为我们需要遍历信任关系更新入度和出度，然后再遍历所有人。
   - 空间复杂度：$O(n)$，因为我们使用了两个大小为 $n+1$ 的数组来存储入度和出度。