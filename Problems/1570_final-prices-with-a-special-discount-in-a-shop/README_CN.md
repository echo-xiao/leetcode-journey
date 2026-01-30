# 1570. 商品折扣后的最终价格

**难度**: Easy | **标签**: `Array` `Stack` `Monotonic Stack`

## 题目描述

<p>给你一个数组&nbsp;<code>prices</code>&nbsp;，其中&nbsp;<code>prices[i]</code>&nbsp;是商店里第&nbsp;<code>i</code>&nbsp;件商品的价格。</p>

<p>商店里正在进行促销活动，如果你要买第&nbsp;<code>i</code>&nbsp;件商品，那么你可以得到与 <code>prices[j]</code> 相等的折扣，其中&nbsp;<code>j</code>&nbsp;是满足&nbsp;<code>j &gt; i</code>&nbsp;且&nbsp;<code>prices[j] &lt;= prices[i]</code>&nbsp;的&nbsp;<strong>最小下标</strong>&nbsp;，如果没有满足条件的&nbsp;<code>j</code>&nbsp;，你将没有任何折扣。</p>

<p>请你返回一个数组，数组中第&nbsp;<code>i</code>&nbsp;个元素是折扣后你购买商品 <code>i</code>&nbsp;最终需要支付的价格。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>prices = [8,4,6,2,3]
<strong>输出：</strong>[4,2,4,2,3]
<strong>解释：</strong>
商品 0 的价格为 price[0]=8 ，你将得到 prices[1]=4 的折扣，所以最终价格为 8 - 4 = 4 。
商品 1 的价格为 price[1]=4 ，你将得到 prices[3]=2 的折扣，所以最终价格为 4 - 2 = 2 。
商品 2 的价格为 price[2]=6 ，你将得到 prices[3]=2 的折扣，所以最终价格为 6 - 2 = 4 。
商品 3 和 4 都没有折扣。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>prices = [1,2,3,4,5]
<strong>输出：</strong>[1,2,3,4,5]
<strong>解释：</strong>在这个例子中，所有商品都没有折扣。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>prices = [10,1,1,6]
<strong>输出：</strong>[9,0,1,6]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 500</code></li>
	<li><code>1 &lt;= prices[i] &lt;= 10^3</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用单调栈结构，在遍历商品价格时，找到每个商品后面第一个小于等于当前价格的商品作为折扣。

2. 综合思路：
   - **单调栈法（从前往后遍历）**：通过一个栈来维护价格的索引，遍历过程中如果发现栈顶元素对应的价格大于等于当前价格，则更新栈顶元素对应的结果为当前价格作为折扣。
   - **单调栈法（从后往前遍历）**：通过一个栈来维护价格，倒序遍历价格列表，栈中保存的是可能作为折扣的价格，遇到比当前价格小的则出栈，更新当前价格的折扣。

3. 全量伪代码：
   - **单调栈法（从前往后遍历）**：
     ```
     初始化结果数组为价格数组的副本
     初始化一个空栈
     对于每个价格及其索引：
         当栈不为空且栈顶元素对应的价格大于等于当前价格：
             弹出栈顶元素索引
             更新结果数组中该索引位置的价格为原价格减去当前价格
         将当前索引压入栈
     返回结果数组
     ```
   - **单调栈法（从后往前遍历）**：
     ```
     初始化结果数组为价格数组的副本
     初始化一个空栈
     从后向前遍历价格数组：
         当栈不为空且栈顶元素大于当前价格：
             弹出栈顶元素
         如果栈不为空：
             更新结果数组中当前索引位置的价格为原价格减去栈顶元素
         将当前价格压入栈
     返回结果数组
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是价格数组的长度，因为每个元素最多只会被压入和弹出栈一次。
   - 空间复杂度：$O(n)$，用于存储结果数组和栈。