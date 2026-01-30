# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]

        inorderIdx = 0

        for i in range(1, len(preorder)):
            prev = preorder[i]
            node = stack[-1]

            if node.val != inorder[inorderIdx]:
                node.left = TreeNode(prev)
                stack.append(node.left)

            else:
                while stack and stack[-1].val == inorder[inorderIdx]:
                    node = stack.pop()
                    inorderIdx += 1
                node.right = TreeNode(prev)
                stack.append(node.right)
        
        return root