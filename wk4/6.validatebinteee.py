# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return Solution.do(root,  float('-inf'),  float('inf'))
    
    # define and upper and lower bound the val must be inbetween
    def do(root, lo, hi):
        if root is None:
            return True
        return Solution.do(root.left, lo, root.val) and Solution.do(root.right, root.val, hi) and root.val < hi and root.val > lo
        