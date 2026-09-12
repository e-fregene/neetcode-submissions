# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS, Go on a level collect from left to right in list
        res=[]
        queue= deque([root])

        if not root:
            return res
            
        res.append([root.val])
        
        while queue:
            level=[]
            for i in range(len(queue)):
                node= queue.popleft()
                if node.left:
                    queue.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    level.append(node.right.val)
            if len(level) > 0:
                res.append(level)
        return res



        