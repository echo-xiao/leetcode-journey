# 605. 种花问题

**难度**: Easy | **标签**: `Array` `Greedy`

## 题目描述

<p>假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。</p>

<p>给你一个整数数组&nbsp;<code>flowerbed</code> 表示花坛，由若干 <code>0</code> 和 <code>1</code> 组成，其中 <code>0</code> 表示没种植花，<code>1</code> 表示种植了花。另有一个数&nbsp;<code>n</code><strong> </strong>，能否在不打破种植规则的情况下种入&nbsp;<code>n</code><strong>&nbsp;</strong>朵花？能则返回 <code>true</code> ，不能则返回 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>flowerbed = [1,0,0,0,1], n = 1
<strong>输出：</strong>true
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>flowerbed = [1,0,0,0,1], n = 2
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= flowerbed.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>flowerbed[i]</code> 为 <code>0</code> 或 <code>1</code></li>
	<li><code>flowerbed</code> 中不存在相邻的两朵花</li>
	<li><code>0 &lt;= n &lt;= flowerbed.length</code></li>
</ul>

---
## 解题思路与复盘

1. 一句话直击本质：通过在花坛的两端添加虚拟空位，遍历花坛数组并检查连续三个位置是否为空以决定是否可以种花。

2. 综合思路：
   - 迭代法：在花坛数组的两端添加虚拟空位（即在数组的开头和结尾各添加一个0），然后遍历数组，检查当前位置及其相邻位置是否都为空（即三个连续位置都是0），如果是，则在当前位置种花并增加计数器，最后判断种花的数量是否达到要求。

3. 全量伪代码：
   ```
   函数 canPlaceFlowers(花坛数组, n):
       在花坛数组的开头和结尾各添加一个0
       初始化种花计数器 res 为0
       从索引1遍历到数组的倒数第二个位置:
           如果当前位置及其前后位置都是0:
               在当前位置种花（将当前位置置为1）
               增加种花计数器 res
       返回 res 是否大于等于 n
   ```

4. 复杂度：
   - 时间复杂度：$O(m)$，其中 $m$ 是花坛数组的长度，因为需要遍历整个数组一次。
   - 空间复杂度：$O(1)$，因为只使用了常数额外空间（不考虑输入数组的空间）。