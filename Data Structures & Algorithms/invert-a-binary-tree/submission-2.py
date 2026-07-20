# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # swap each left child with the right child
        # continue this through each level of the tree, keeping the root

        if not root: 
            return None

        # swap the children
        swap = root.right
        root.right = root.left
        root.left = swap

        # invert the left subtree and right subtree
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root 

        # T





















         # time: O(n)
        # space: O(n)
        if not root: 
            return None
        
        # swap all the children (DFS)
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
       
 

        
