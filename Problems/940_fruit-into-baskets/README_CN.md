# 940. 水果成篮

**难度**: Medium | **标签**: `Array` `Hash Table` `Sliding Window`

## 题目描述

<p>你正在探访一家农场，农场从左到右种植了一排果树。这些树用一个整数数组 <code>fruits</code> 表示，其中 <code>fruits[i]</code> 是第 <code>i</code> 棵树上的水果 <strong>种类</strong> 。</p>

<p>你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果：</p>

<ul>
	<li>你只有 <strong>两个</strong> 篮子，并且每个篮子只能装 <strong>单一类型</strong> 的水果。每个篮子能够装的水果总量没有限制。</li>
	<li>你可以选择任意一棵树开始采摘，你必须从 <strong>每棵</strong> 树（包括开始采摘的树）上 <strong>恰好摘一个水果</strong> 。采摘的水果应当符合篮子中的水果类型。每采摘一次，你将会向右移动到下一棵树，并继续采摘。</li>
	<li>一旦你走到某棵树前，但水果不符合篮子的水果类型，那么就必须停止采摘。</li>
</ul>

<p>给你一个整数数组 <code>fruits</code> ，返回你可以收集的水果的 <strong>最大</strong> 数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>fruits = [<em><strong>1,2,1</strong></em>]
<strong>输出：</strong>3
<strong>解释：</strong>可以采摘全部 3 棵树。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>fruits = [0,<em><strong>1,2,2</strong></em>]
<strong>输出：</strong>3
<strong>解释：</strong>可以采摘 [1,2,2] 这三棵树。
如果从第一棵树开始采摘，则只能采摘 [0,1] 这两棵树。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>fruits = [1,<em><strong>2,3,2,2</strong></em>]
<strong>输出：</strong>4
<strong>解释：</strong>可以采摘 [2,3,2,2] 这四棵树。
如果从第一棵树开始采摘，则只能采摘 [1,2] 这两棵树。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>fruits = [3,3,3,<em><strong>1,2,1,1,2</strong></em>,3,3,4]
<strong>输出：</strong>5
<strong>解释：</strong>可以采摘 [1,2,1,1,2] 这五棵树。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= fruits.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= fruits[i] &lt; fruits.length</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是使用滑动窗口维护最多包含两种不同水果的最大子数组长度。

2. 综合思路：
   - 滑动窗口：通过两个指针（`left` 和 `right`）构建一个动态窗口，窗口内最多包含两种不同的水果类型，并在移动过程中更新最大长度。
   - 哈希表：使用哈希表记录当前窗口内每种水果的数量，当窗口内水果种类超过两种时，调整左指针以保持窗口有效。

3. 全量伪代码：
   ```
   定义函数 totalFruit，输入为水果列表 fruits
       初始化左指针 left 为 0
       初始化右指针 right 为 0
       初始化哈希表 res 为空
       初始化最大长度 maxSum 为 0

       当右指针小于水果列表长度时，执行以下步骤：
           将 fruits[right] 加入哈希表 res，计数加一
           右指针右移一位

           当哈希表 res 中的水果种类数大于 2 时，执行以下步骤：
               将 fruits[left] 在哈希表中计数减一
               如果 fruits[left] 的计数为 0，则从哈希表中删除该水果
               左指针右移一位

           更新 maxSum 为当前 maxSum 和 (right - left) 的较大值

       返回 maxSum
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是水果列表的长度，因为每个水果最多被访问两次（一次被右指针访问，一次被左指针移出窗口）。
   - 空间复杂度：$O(1)$，因为哈希表中最多存储两种水果的计数。