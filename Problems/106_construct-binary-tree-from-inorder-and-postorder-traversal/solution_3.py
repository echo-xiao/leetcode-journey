# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])

        rootPos = inorder.index(root.val)

        leftIn = inorder[:rootPos]
        rightIn = inorder[rootPos+1:]

        leftPost = postorder[:len(leftIn)]
        rightPost = postorder[len(leftIn): -1]

        root.left = self.buildTree(leftIn, leftPost)
        root.right = self.buildTree(rightIn, rightPost)

        return root

