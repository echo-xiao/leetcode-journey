# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        node = TreeNode(preorder[0])

        midIdx = inorder.index(node.val)

        leftPre = preorder[1:1+midIdx]
        rightPre = preorder[1+midIdx:]

        leftIn = inorder[0: midIdx]
        rightIn = inorder[midIdx+1:]
        
        node.left = self.buildTree(leftPre, leftIn)
        node.right = self.buildTree(rightPre, rightIn)

        return node