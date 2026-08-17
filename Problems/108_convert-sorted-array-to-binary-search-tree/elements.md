# 108. 将有序数组转换为二叉搜索树 · 要素

1. 函数定义：build(left, right) 表示用 nums 下标 left 到 right 这段有序区间造一棵平衡 BST，返回这棵子树的根节点。

2. base case：当 left > right（区间为空）时返回 None，表示这里挂空子树。

3. 单层主体：取 mid=(left+right)//2，用 nums[mid] 新建根节点，然后把 build(left,mid-1) 挂到 root.left、build(mid+1,right) 挂到 root.right，返回 root。

4. 代码位置：前序位置：先建当前根节点再递归造左右子树（若用索引模拟中序那种写法，则是先递归左、再取值建根、再递归右的中序位置）。
