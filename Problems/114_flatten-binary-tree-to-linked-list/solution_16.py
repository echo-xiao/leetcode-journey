class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        
        while curr:
            # 如果有左子树，才需要搬运
            if curr.left:

                # 找到左子树的最右节点（predecessor）
                predecessor = curr.left

                while predecessor.right:
                    predecessor = predecessor.right
                
                # 把原来的右子树，接到predecessor后面
                predecessor.right = curr.right
                
                # 把左子树移到右边，左边置空
                curr.right = curr.left
                curr.left = None
                
            # 继续处理下一个节点，现在都在右边了
            curr = curr.right