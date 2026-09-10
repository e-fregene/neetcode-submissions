# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.same_tree(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot))

    def same_tree(self, R, S):
        if not R and not S:
            return True

        if not R or not S:
            return False

        if R and S and R.val==S.val:
            return (self.same_tree(R.left, S.left) and self.same_tree(R.right, S.right))
        else:
            return False   


            
        