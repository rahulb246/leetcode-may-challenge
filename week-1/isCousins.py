# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
# Return true if and only if the nodes corresponding to the values x and y are cousins.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def haveSameParents(self, root, x, y): 
        if not root: 
            return 0
        
        return ((root.left and root.right and ((root.left.val == x and root.right.val == y) or 
                (root.left.val == y and root.right.val == x))) or
                self.haveSameParents(root.left, x, y) or
                self.haveSameParents(root.right, x, y))
    
    def depth(self, root, val, dpt):   
        if not root: 
            return 0 
        if root.val == val:  
            return dpt 

        d = self.depth(root.left, val, dpt+1) 
        return d if (d != 0) else self.depth(root.right, val, dpt+1)
    
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        return 1 if((self.depth(root, x, 1) == self.depth(root, y, 1)) and 
             (not self.haveSameParents(root, x, y))) else 0 
