# 2199. 两栋颜色不同且距离最远的房子

**难度**: Easy | **标签**: `Array` `Greedy`

## 题目描述

<p>街上有 <code>n</code> 栋房子整齐地排成一列，每栋房子都粉刷上了漂亮的颜色。给你一个下标从 <strong>0</strong> 开始且长度为 <code>n</code> 的整数数组 <code>colors</code> ，其中 <code>colors[i]</code> 表示第&nbsp; <code>i</code> 栋房子的颜色。</p>

<p>返回 <strong>两栋</strong> 颜色 <strong>不同</strong> 房子之间的 <strong>最大</strong> 距离。</p>

<p>第 <code>i</code> 栋房子和第 <code>j</code> 栋房子之间的距离是 <code>abs(i - j)</code> ，其中 <code>abs(x)</code> 是 <code>x</code> 的绝对值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/10/31/eg1.png" style="width: 610px; height: 84px;" /></p>

<pre>
<strong>输入：</strong>colors = [<strong><em>1</em></strong>,1,1,<em><strong>6</strong></em>,1,1,1]
<strong>输出：</strong>3
<strong>解释：</strong>上图中，颜色 1 标识成蓝色，颜色 6 标识成红色。
两栋颜色不同且距离最远的房子是房子 0 和房子 3 。
房子 0 的颜色是颜色 1 ，房子 3 的颜色是颜色 6 。两栋房子之间的距离是 abs(0 - 3) = 3 。
注意，房子 3 和房子 6 也可以产生最佳答案。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/10/31/eg2.png" style="width: 426px; height: 84px;" /></p>

<pre>
<strong>输入：</strong>colors = [<em><strong>1</strong></em>,8,3,8,<em><strong>3</strong></em>]
<strong>输出：</strong>4
<strong>解释：</strong>上图中，颜色 1 标识成蓝色，颜色 8 标识成黄色，颜色 3 标识成绿色。
两栋颜色不同且距离最远的房子是房子 0 和房子 4 。
房子 0 的颜色是颜色 1 ，房子 4 的颜色是颜色 3 。两栋房子之间的距离是 abs(0 - 4) = 4 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>colors = [<em><strong>0</strong></em>,<em><strong>1</strong></em>]
<strong>输出：</strong>1
<strong>解释：</strong>两栋颜色不同且距离最远的房子是房子 0 和房子 1 。
房子 0 的颜色是颜色 0 ，房子 1 的颜色是颜色 1 。两栋房子之间的距离是 abs(0 - 1) = 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n ==&nbsp;colors.length</code></li>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>0 &lt;= colors[i] &lt;= 100</code></li>
	<li>生成的测试数据满足 <strong>至少 </strong>存在 2 栋颜色不同的房子</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过从两端向中间扫描找到与两端颜色不同的房子，计算最大距离。

2. 综合思路：
   - 双指针法：从数组的两端分别向中间扫描，找到与两端颜色不同的房子，计算两者之间的最大距离。

3. 全量伪代码：
   ```plaintext
   定义函数 maxDistance，输入为颜色列表 colors
       初始化指针 i 为 0，指针 j 为 colors 的最后一个索引
       
       从左向右扫描：
           当 i 小于 colors 的长度时：
               如果 colors[i] 与 colors 的最后一个元素不同：
                   计算 dis1 为 colors 的长度减去 i 减 1
                   跳出循环
               i 增加 1

       从右向左扫描：
           当 j 大于 0 时：
               如果 colors[j] 与 colors 的第一个元素不同：
                   计算 dis2 为 j
                   跳出循环
               j 减少 1

       计算 dis 为 dis1 和 dis2 中的较大值
       返回 dis
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，因为最多需要遍历整个列表两次。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外变量。