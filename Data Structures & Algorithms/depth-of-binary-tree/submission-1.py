# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        L=1
        R=1

        if not root:
            return 0

        if root.right!=None:
            L= 1+ self.maxDepth(root.right)
        if root.left!=None:
            R= 1+ self.maxDepth(root.left)

        return max(L,R)
        