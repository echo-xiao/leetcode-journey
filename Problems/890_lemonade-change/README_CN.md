# 890. 柠檬水找零

**难度**: Easy | **标签**: `Array` `Greedy`

## 题目描述

<p>在柠檬水摊上，每一杯柠檬水的售价为&nbsp;<code>5</code>&nbsp;美元。顾客排队购买你的产品，（按账单 <code>bills</code> 支付的顺序）一次购买一杯。</p>

<p>每位顾客只买一杯柠檬水，然后向你付 <code>5</code> 美元、<code>10</code> 美元或 <code>20</code> 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 <code>5</code> 美元。</p>

<p>注意，一开始你手头没有任何零钱。</p>

<p>给你一个整数数组 <code>bills</code> ，其中 <code>bills[i]</code> 是第 <code>i</code> 位顾客付的账。如果你能给每位顾客正确找零，返回&nbsp;<code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>bills = [5,5,5,10,20]
<strong>输出：</strong>true
<strong>解释：
</strong>前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>bills = [5,5,10,10,20]
<strong>输出：</strong>false
<strong>解释：</strong>
前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
由于不是每位顾客都得到了正确的找零，所以答案是 false。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= bills.length &lt;= 10<sup>5</sup></code></li>
	<li><code>bills[i]</code>&nbsp;不是&nbsp;<code>5</code>&nbsp;就是&nbsp;<code>10</code>&nbsp;或是&nbsp;<code>20</code>&nbsp;</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过维护手头的5美元和10美元的数量，确保在每次交易时能正确找零。

2. **综合思路：** 
   - 迭代法：遍历每一笔交易，根据顾客支付的金额（5、10、20美元），更新手头的5美元和10美元的数量，并在无法找零时返回False。

3. **全量伪代码：**

   ```plaintext
   初始化5美元数量 rem5 为 0
   初始化10美元数量 rem10 为 0

   对于每一笔交易金额 m 在交易列表 bills 中：
       如果 m 是 5：
           增加 rem5 的数量
       如果 m 是 10：
           如果 rem5 小于等于 0：
               返回 False
           否则：
               减少 rem5 的数量
               增加 rem10 的数量
       如果 m 是 20：
           如果 rem5 大于 0 且 rem10 大于 0：
               减少 rem5 和 rem10 的数量
           否则如果 rem5 大于等于 3：
               减少 rem5 的数量 3 次
           否则：
               返回 False

   返回 True
   ```

4. **复杂度：**

   - 时间复杂度：$O(n)$，其中 $n$ 是交易列表的长度，因为我们需要遍历每一笔交易。
   - 空间复杂度：$O(1)$，因为我们只使用了固定数量的额外空间来存储5美元和10美元的数量。