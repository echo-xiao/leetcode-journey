# 1436. 获取你好友已观看的视频

**难度**: Medium | **标签**: `Array` `Hash Table` `Breadth-First Search` `Graph Theory` `Sorting`

**归类**: 8. 常用数据结构 > Array

## 题目描述

<p>有&nbsp;<code>n</code> 个人，每个人都有一个&nbsp; <code>0</code>&nbsp;到&nbsp;<code>n-1</code>&nbsp;的唯一&nbsp;<em>id</em>&nbsp;。</p>

<p>给你数组 <code>watchedVideos</code>&nbsp; 和&nbsp;<code>friends</code>&nbsp;，其中&nbsp;<code>watchedVideos[i]</code>&nbsp; 和&nbsp;<code>friends[i]</code>&nbsp;分别表示&nbsp;<code>id = i</code>&nbsp;的人观看过的视频列表和他的好友列表。</p>

<p>Level&nbsp;<strong>1</strong>&nbsp;的视频包含所有你好友观看过的视频，level&nbsp;<strong>2</strong>&nbsp;的视频包含所有你好友的好友观看过的视频，以此类推。一般的，Level 为 <strong>k</strong>&nbsp;的视频包含所有从你出发，最短距离为&nbsp;<strong>k</strong>&nbsp;的好友观看过的视频。</p>

<p>给定你的&nbsp;<code>id</code>&nbsp; 和一个&nbsp;<code>level</code>&nbsp;值，请你找出所有指定 <code>level</code> 的视频，并将它们按观看频率升序返回。如果有频率相同的视频，请将它们按字母顺序从小到大排列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/03/leetcode_friends_1.png" style="height: 179px; width: 129px;"></strong></p>

<pre><strong>输入：</strong>watchedVideos = [[&quot;A&quot;,&quot;B&quot;],[&quot;C&quot;],[&quot;B&quot;,&quot;C&quot;],[&quot;D&quot;]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
<strong>输出：</strong>[&quot;B&quot;,&quot;C&quot;] 
<strong>解释：</strong>
你的 id 为 0（绿色），你的朋友包括（黄色）：
id 为 1 -&gt; watchedVideos = [&quot;C&quot;]&nbsp;
id 为 2 -&gt; watchedVideos = [&quot;B&quot;,&quot;C&quot;]&nbsp;
你朋友观看过视频的频率为：
B -&gt; 1&nbsp;
C -&gt; 2
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/03/leetcode_friends_2.png" style="height: 179px; width: 129px;"></strong></p>

<pre><strong>输入：</strong>watchedVideos = [[&quot;A&quot;,&quot;B&quot;],[&quot;C&quot;],[&quot;B&quot;,&quot;C&quot;],[&quot;D&quot;]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
<strong>输出：</strong>[&quot;D&quot;]
<strong>解释：</strong>
你的 id 为 0（绿色），你朋友的朋友只有一个人，他的 id 为 3（黄色）。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == watchedVideos.length ==&nbsp;friends.length</code></li>
	<li><code>2 &lt;= n&nbsp;&lt;= 100</code></li>
	<li><code>1 &lt;=&nbsp;watchedVideos[i].length &lt;= 100</code></li>
	<li><code>1 &lt;=&nbsp;watchedVideos[i][j].length &lt;= 8</code></li>
	<li><code>0 &lt;= friends[i].length &lt; n</code></li>
	<li><code>0 &lt;= friends[i][j]&nbsp;&lt; n</code></li>
	<li><code>0 &lt;= id &lt; n</code></li>
	<li><code>1 &lt;= level &lt; n</code></li>
	<li>如果&nbsp;<code>friends[i]</code> 包含&nbsp;<code>j</code>&nbsp;，那么&nbsp;<code>friends[j]</code> 包含&nbsp;<code>i</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法通过广度优先搜索（BFS）找到指定层级的好友，然后统计并排序这些好友观看的视频。

2. 综合思路：
   - **广度优先搜索（BFS）**：使用队列进行层次遍历，以找到指定层级的好友。
   - **计数与排序**：利用计数器统计视频观看次数，并按观看次数和字典序排序。

3. 全量伪代码：
   ```plaintext
   定义函数 watchedVideosByFriends(已观看视频列表, 好友关系列表, 用户ID, 层级):
       初始化访问标记列表为 False
       将用户ID标记为已访问
       初始化队列，存入 (用户ID, 层级)
       初始化结果列表

       当队列不为空时:
           弹出队列头部元素 (当前用户ID, 当前层级)
           
           如果当前层级为 0:
               将当前用户ID加入结果列表
               继续下一个循环

           对于当前用户的每个好友:
               如果该好友未被访问:
                   标记该好友为已访问
                   将 (好友ID, 当前层级减一) 加入队列

       初始化计数器
       对于结果列表中的每个用户:
           对于该用户观看的每个视频:
               增加视频的计数

       将计数器中的视频按观看次数和字典序排序
       返回排序后的视频列表

   ```

4. 复杂度：
   - 时间复杂度：$O(n + m \log m)$，其中 $n$ 是好友关系的总数，$m$ 是视频的总数。
   - 空间复杂度：$O(n + m)$，用于存储访问标记、队列和计数器。