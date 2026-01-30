# 867. 新 21 点

**难度**: Medium | **标签**: `Math` `Dynamic Programming` `Sliding Window` `Probability and Statistics`

## 题目描述

<p>爱丽丝参与一个大致基于纸牌游戏 <strong>“21点”</strong> 规则的游戏，描述如下：</p>

<p>爱丽丝以 <code>0</code> 分开始，并在她的得分少于 <code>k</code> 分时抽取数字。 抽取时，她从 <code>[1, maxPts]</code> 的范围中随机获得一个整数作为分数进行累计，其中 <code>maxPts</code> 是一个整数。 每次抽取都是独立的，其结果具有相同的概率。</p>

<p>当爱丽丝获得 <code>k</code> 分 <strong>或更多分</strong> 时，她就停止抽取数字。</p>

<p>爱丽丝的分数不超过 <code>n</code> 的概率是多少？</p>

<p>与实际答案误差不超过&nbsp;<code>10<sup>-5</sup></code> 的答案将被视为正确答案。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 10, k = 1, maxPts = 10
<strong>输出：</strong>1.00000
<strong>解释：</strong>爱丽丝得到一张牌，然后停止。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 6, k = 1, maxPts = 10
<strong>输出：</strong>0.60000
<strong>解释：</strong>爱丽丝得到一张牌，然后停止。 在 10 种可能性中的 6 种情况下，她的得分不超过 6 分。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 21, k = 17, maxPts = 10
<strong>输出：</strong>0.73278
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= k &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= maxPts &lt;= 10<sup>4</sup></code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过动态规划和滑动窗口技术计算从0开始不超过n的概率。

2. **综合思路：**
   - **动态规划与滑动窗口：** 通过动态规划数组 `dp` 记录每个点数的概率，并使用滑动窗口技术来优化计算，避免重复计算。
   - **优化的动态规划：** 使用字典来存储动态规划结果，减少空间复杂度，同时通过计算窗口和来更新概率。

3. **全量伪代码：**

   - **动态规划与滑动窗口：**
     ```
     如果 k 为 0 或者 n 大于等于 k + maxPts:
         返回 1.0
     初始化 dp 数组，长度为 n+1，所有元素为 0.0
     设置 dp[0] 为 1.0
     初始化 windowSum 为 1.0
     初始化 res 为 0.0
     对于 i 从 1 到 n:
         设置 dp[i] 为 windowSum / maxPts
         如果 i 大于等于 k:
             将 dp[i] 加到 res
         如果 i 小于 k:
             将 dp[i] 加到 windowSum
         如果 i 大于等于 maxPts:
             从 windowSum 中减去 dp[i-maxPts]
     返回 res
     ```

   - **优化的动态规划：**
     ```
     如果 k 为 0:
         返回 1.0
     初始化 windowSum 为 0
     对于 i 从 k 到 k + maxPts:
         如果 i 小于等于 n:
             将 1 加到 windowSum
     初始化 dp 字典
     对于 i 从 k-1 到 0:
         设置 dp[i] 为 windowSum / maxPts
         如果 i + maxPts 小于等于 n:
             从 windowSum 中减去 dp[i + maxPts] 或 1
         将 dp[i] 加到 windowSum
     返回 dp[0]
     ```

4. **复杂度：**

   - **时间复杂度：** $O(n)$
   - **空间复杂度：** $O(n)$ (对于版本1和2) 或 $O(k)$ (对于版本3)