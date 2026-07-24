# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count= 0
        if not root:
            return count

        right_side= 1+self.maxDepth(root.right)
        left_side= 1+self.maxDepth(root.left)

        if left_side>right_side:
            return left_side
        else:
            return right_side
        