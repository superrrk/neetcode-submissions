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
        
        # subtrees need to be equal 
        if p and q and p.val == q.val: 
            # recursively call each l and r node
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else: 
            return False
        
        # recursive DFS 

        