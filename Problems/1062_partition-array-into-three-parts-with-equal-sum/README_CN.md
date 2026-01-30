# 1062. 将数组分成和相等的三个部分

**难度**: Easy | **标签**: `Array` `Greedy`

## 题目描述

<p>给你一个整数数组 <code>arr</code>，只有可以将其划分为三个和相等的 <strong>非空</strong> 部分时才返回 <code>true</code>，否则返回 <code>false</code>。</p>

<p>形式上，如果可以找出索引 <code>i + 1 < j</code> 且满足 <code>(arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])</code> 就可以将数组三等分。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [0,2,1,-6,6,-7,9,1,2,0,1]
<strong>输出：</strong>true
<strong>解释：</strong>0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [0,2,1,-6,6,7,9,-1,2,0,1]
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [3,3,6,5,-2,2,5,1,-9,4]
<strong>输出：</strong>true
<strong>解释：</strong>3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 <= arr.length <= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> <= arr[i] <= 10<sup>4</sup></code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过遍历数组累加元素，判断是否能找到三个子数组，其和等于总和的三分之一。

2. **综合思路：**
   - **迭代法：** 计算数组总和，若不能被3整除则返回False；否则遍历数组，累加元素并检查累加和是否等于目标值（总和的三分之一），计数达到3次则返回True。
   - **变体思路：** 在某些版本中，优化了判断条件，提前返回True以减少不必要的遍历。

3. **全量伪代码：**

   ```plaintext
   定义函数 canThreePartsEqualSum(arr):
       计算数组总和 sumArr
       如果 sumArr 不能被 3 整除:
           返回 False

       计算目标和 targetSum = sumArr / 3
       初始化当前和 curr = 0
       初始化计数器 cnt = 0

       对于数组中的每个元素 num:
           将 num 加入 curr
           如果 curr 等于 targetSum:
               增加计数器 cnt
               重置 curr = 0
               如果 cnt 等于 3:
                   返回 True

       返回 cnt 是否大于等于 3
   ```

4. **复杂度：**
   - 时间复杂度：$O(n)$，因为需要遍历整个数组一次。
   - 空间复杂度：$O(1)$，只使用了常数个额外变量。