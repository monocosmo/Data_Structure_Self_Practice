"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        paths = []
        
        if root is None:
            return paths
        
        if root.left is None and root.right is None:
            paths.append(str(root.val))
            return paths
        
        leftPaths = self.binaryTreePaths(root.left)
        rightPaths = self.binaryTreePaths(root.right)
        
        for path in leftPaths:
            paths.append(str(root.val) + '->' + path)
        for path in rightPaths:
            paths.append(str(root.val) + '->' + path)
        
        return paths
