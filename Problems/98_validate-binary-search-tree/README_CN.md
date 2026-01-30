# 98. 验证二叉搜索树

**难度**: Medium | **标签**: `Tree` `Depth-First Search` `Binary Search Tree` `Binary Tree`

## 题目描述

<p>给你一个二叉树的根节点 <code>root</code> ，判断其是否是一个有效的二叉搜索树。</p>

<p><strong>有效</strong> 二叉搜索树定义如下：</p>

<ul>
	<li>节点的左<span data-keyword="subtree">子树</span>只包含<strong>&nbsp;严格小于 </strong>当前节点的数。</li>
	<li>节点的右子树只包含 <strong>严格大于</strong> 当前节点的数。</li>
	<li>所有左子树和右子树自身必须也是二叉搜索树。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg" style="width: 302px; height: 182px;" />
<pre>
<strong>输入：</strong>root = [2,1,3]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg" style="width: 422px; height: 292px;" />
<pre>
<strong>输入：</strong>root = [5,1,4,null,null,3,6]
<strong>输出：</strong>false
<strong>解释：</strong>根节点的值是 5 ，但是右子节点的值是 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目范围在<code>[1, 10<sup>4</sup>]</code> 内</li>
	<li><code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


---
## 解题思路与复盘

### 一句话直击本质
验证二叉搜索树的核心逻辑是确保每个节点的值在其允许的范围内，并通过中序遍历检查节点值是否严格递增。

### 综合思路
1. **递归验证范围法**：通过递归检查每个节点的值是否在其允许的范围内（由其父节点的值决定），这是通过传递上下界来实现的。
2. **中序遍历法**：
   - **递归中序遍历**：利用中序遍历的特性，检查节点值是否严格递增。
   - **迭代中序遍历**：使用栈模拟中序遍历，检查节点值是否严格递增。

### 全量伪代码
#### 递归验证范围法
```plaintext
函数 isValidBST(根节点):
    返回 validate(根节点, 负无穷, 正无穷)

函数 validate(节点, 下界, 上界):
    如果 节点为空:
        返回 真
    如果 节点值 <= 下界 或 节点值 >= 上界:
        返回 假
    返回 validate(节点的左子节点, 下界, 节点值) 且 validate(节点的右子节点, 节点值, 上界)
```

#### 递归中序遍历法
```plaintext
函数 isValidBST(根节点):
    初始化 prev 为 负无穷
    返回 inorder(根节点)

函数 inorder(节点):
    如果 节点为空:
        返回 真
    如果 不满足 inorder(节点的左子节点):
        返回 假
    如果 prev >= 节点值:
        返回 假
    更新 prev 为 节点值
    返回 inorder(节点的右子节点)
```

#### 迭代中序遍历法
```plaintext
函数 isValidBST(根节点):
    初始化 栈为空, curr 为 根节点, prev 为 负无穷
    当 curr 不为空 或 栈不为空:
        当 curr 不为空:
            将 curr 压入栈
            curr 移动到其左子节点
        从栈中弹出节点 赋值给 curr
        如果 prev 不为空 且 curr.val <= prev.val:
            返回 假
        更新 prev 为 curr
        curr 移动到其右子节点
    返回 真
```

### 复杂度
- **时间复杂度**: 所有方法的时间复杂度均为 $O(n)$，其中 $n$ 是二叉树中的节点数，因为每个节点都需要访问一次。
- **空间复杂度**:
  - **递归验证范围法**: $O(h)$，其中 $h$ 是树的高度，递归调用栈的深度。
  - **递归中序遍历法**: $O(h)$，递归调用栈的深度。
  - **迭代中序遍历法**: $O(h)$，栈的最大深度。