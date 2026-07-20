# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # global variable is accessible within helper function 
        self.res = 0

        # returns height
        def dfs(curr): 
            if not curr: 
                return 0 
        
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)


        # for each node, computer its L, R subtree and diameter through that node 
        
        # recursively find the diameter of L and R subtree 

        # the final diameter for this node is the max of 
        
        dfs(root)
        return self.res


