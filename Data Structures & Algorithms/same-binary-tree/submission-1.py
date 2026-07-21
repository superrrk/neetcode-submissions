# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # want to check that the tree structure and values are equal

        # check if root nodes are both empty
        if not p and not q: 
            return True

        # base case: subtrees need to be equal 
        if not p or not q or p.val != q.val:
            return False
        
         # recursively call each l and r node
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # recursive DFS 

        