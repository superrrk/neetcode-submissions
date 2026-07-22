# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case: both of the trees are not empty
        # a null subtree is the same as a null tree, technically the root tree has null 
        # children with a null subtree
        if not subRoot:
            return True
        if not root: 
            return False

        if self.sameTree(root, subRoot):
            return True
        # we can compare the subRoot to the left of root and the right of root subtrees
        # we call if the left subtree is a subtree fo the subroot
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))

    def sameTree(self, root, subRoot):
        # a null subtree is the same as a null tree
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                   self.sameTree(root.right, subRoot.right))
        return False