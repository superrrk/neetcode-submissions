# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # queue up the notes to count the 

        # if node is none, depth is 0 
        if root is None: 
            return 0

        # recursively computer left depth and right depth
        # the depth is at least 1 because of the root node
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
