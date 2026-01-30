# 861. 翻转图像

**难度**: Easy | **标签**: `Array` `Two Pointers` `Bit Manipulation` `Matrix` `Simulation`

## 题目描述

<p>给定一个<meta charset="UTF-8" />&nbsp;<code>n x n</code>&nbsp;的二进制矩阵&nbsp;<code>image</code>&nbsp;，先 <strong>水平</strong> 翻转图像，然后&nbsp;<strong>反转&nbsp;</strong>图像并返回&nbsp;<em>结果</em>&nbsp;。</p>

<p><strong>水平</strong>翻转图片就是将图片的每一行都进行翻转，即逆序。</p>

<ul>
	<li>例如，水平翻转&nbsp;<code>[1,1,0]</code>&nbsp;的结果是&nbsp;<code>[0,1,1]</code>。</li>
</ul>

<p><strong>反转</strong>图片的意思是图片中的&nbsp;<code>0</code>&nbsp;全部被&nbsp;<code>1</code>&nbsp;替换，&nbsp;<code>1</code>&nbsp;全部被&nbsp;<code>0</code>&nbsp;替换。</p>

<ul>
	<li>例如，反转&nbsp;<code>[0,1,1]</code>&nbsp;的结果是&nbsp;<code>[1,0,0]</code>。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>image = [[1,1,0],[1,0,1],[0,0,0]]
<strong>输出：</strong>[[1,0,0],[0,1,0],[1,1,1]]
<strong>解释：</strong>首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
     然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
<strong>输出：</strong>[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
<strong>解释：</strong>首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
     然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<p><meta charset="UTF-8" /></p>

<ul>
	<li><code>n == image.length</code></li>
	<li><code>n == image[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>images[i][j]</code>&nbsp;==&nbsp;<code>0</code>&nbsp;或&nbsp;<code>1</code>.</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过双指针法翻转每一行，然后逐位取反实现图像的翻转与反转。

2. 综合思路：
   - 迭代法：使用双指针法逐行翻转图像，然后遍历整个图像矩阵，将每个元素取反。

3. 全量伪代码：
   ```plaintext
   定义函数 flipAndInvertImage(输入图像):
       对于每一行 i 从 0 到 图像的长度:
           初始化左指针 left 为 0
           初始化右指针 right 为 图像长度减 1
           当 left 小于 right 时:
               交换图像第 i 行的 left 和 right 位置的元素
               将 left 增加 1
               将 right 减少 1
       
       对于每一行 i 从 0 到 图像的长度:
           对于每一列 j 从 0 到 图像的长度:
               如果图像第 i 行第 j 列的元素是 1:
                   将其置为 0
               否则:
                   将其置为 1
       
       返回图像
   ```

4. 复杂度：
   - 时间复杂度：$\mathcal{O}(n^2)$，其中 $n$ 是图像的边长，因为需要遍历整个图像矩阵两次。
   - 空间复杂度：$\mathcal{O}(1)$，因为算法在原地修改图像，没有使用额外的空间。