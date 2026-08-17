# 108. 将有序数组转换为二叉搜索树 · 解题思路与伪代码

1. **一句话直击本质：**  
   将有序数组的中间元素作为根节点，递归地对左右子数组重复此过程，构建平衡二叉搜索树。

2. **综合思路：**  
   - **递归方法：**  
     通过递归地选择数组的中间元素作为根节点，左半部分作为左子树，右半部分作为右子树，直到数组为空。
   - **模拟中序遍历：**  
     通过递归构建左子树后，使用一个索引来选择当前根节点，然后构建右子树，模拟中序遍历的顺序。

3. **全量伪代码：**

   - **递归方法：**
     ```
     函数 sortedArrayToBST(数组 nums):
         如果 nums 为空:
             返回 None
         设 mid 为 nums 的中间索引
         创建根节点 root，值为 nums[mid]
         root.left 赋值为 sortedArrayToBST(nums 的左半部分)
         root.right 赋值为 sortedArrayToBST(nums 的右半部分)
         返回 root
     ```

   - **模拟中序遍历：**
     ```
     函数 sortedArrayToBST(数组 nums):
         初始化索引 index 为 0
         返回 build(0, len(nums) - 1)

     函数 build(整数 left, 整数 right):
         如果 left > right:
             返回 None
         设 mid 为 (left + right) // 2
         递归构建左子树 leftTree = build(left, mid - 1)
         创建根节点 root，值为 nums[index]
         增加 index
         root.left 赋值为 leftTree
         root.right 赋值为 build(mid + 1, right)
         返回 root
     ```

4. **复杂度：**  
   - 时间复杂度：$O(n)$，其中 $n$ 是数组的长度，因为每个元素都被访问一次。
   - 空间复杂度：$O(\log n)$，用于递归调用栈的空间，最坏情况下是树的高度。
