# 506. 相对名次

**难度**: Easy | **标签**: `Array` `Sorting` `Heap (Priority Queue)`

## 题目描述

<p>给你一个长度为 <code>n</code> 的整数数组 <code>score</code> ，其中 <code>score[i]</code> 是第 <code>i</code> 位运动员在比赛中的得分。所有得分都 <strong>互不相同</strong> 。</p>

<p>运动员将根据得分 <strong>决定名次</strong> ，其中名次第 <code>1</code> 的运动员得分最高，名次第 <code>2</code> 的运动员得分第 <code>2</code> 高，依此类推。运动员的名次决定了他们的获奖情况：</p>

<ul>
	<li>名次第 <code>1</code> 的运动员获金牌 <code>"Gold Medal"</code> 。</li>
	<li>名次第 <code>2</code> 的运动员获银牌 <code>"Silver Medal"</code> 。</li>
	<li>名次第 <code>3</code> 的运动员获铜牌 <code>"Bronze Medal"</code> 。</li>
	<li>从名次第 <code>4</code> 到第 <code>n</code> 的运动员，只能获得他们的名次编号（即，名次第 <code>x</code> 的运动员获得编号 <code>"x"</code>）。</li>
</ul>

<p>使用长度为 <code>n</code> 的数组 <code>answer</code> 返回获奖，其中 <code>answer[i]</code> 是第 <code>i</code> 位运动员的获奖情况。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>score = [5,4,3,2,1]
<strong>输出：</strong>["Gold Medal","Silver Medal","Bronze Medal","4","5"]
<strong>解释：</strong>名次为 [1<sup>st</sup>, 2<sup>nd</sup>, 3<sup>rd</sup>, 4<sup>th</sup>, 5<sup>th</sup>] 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>score = [10,3,8,9,4]
<strong>输出：</strong>["Gold Medal","5","Bronze Medal","Silver Medal","4"]
<strong>解释：</strong>名次为 [1<sup>st</sup>, 5<sup>th</sup>, 3<sup>rd</sup>, 2<sup>nd</sup>, 4<sup>th</sup>] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == score.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= score[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>score</code> 中的所有值 <strong>互不相同</strong></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 使用最大堆对分数进行排序，以确定每个分数的相对名次。

2. **综合思路：**
   - **最大堆排序法：** 将所有分数以负值形式插入最大堆中，以便按从大到小的顺序弹出元素，然后根据弹出顺序分配相应的名次（如金、银、铜牌或具体名次数字）。

3. **全量伪代码：**

   ```plaintext
   定义函数 findRelativeRanks(score):
       初始化空列表 maxHeap
       对于每个分数及其索引 (idx, val) 在 score 中:
           将 (-val, idx) 插入 maxHeap

       初始化结果列表 res，长度为 score 的长度
       初始化名次 place 为 1

       当 maxHeap 非空时:
           弹出 maxHeap 的顶部元素，获取其索引 pos
           如果 place 为 1:
               rank = "Gold Medal"
           否则如果 place 为 2:
               rank = "Silver Medal"
           否则如果 place 为 3:
               rank = "Bronze Medal"
           否则:
               rank = 转换 place 为字符串

           将 rank 赋值给 res[pos]
           place 增加 1

       返回 res
   ```

4. **复杂度：**

   - 时间复杂度：$O(n \log n)$，其中 $n$ 是分数列表的长度。构建最大堆和从堆中弹出元素的操作均为 $O(\log n)$，总共进行 $n$ 次。
   - 空间复杂度：$O(n)$，用于存储最大堆和结果列表。