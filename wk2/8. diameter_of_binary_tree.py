# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        return self.do(root)[0]
    
    def do(self, root): # (max, height)
        if root is None:
            return [0, 0]
        l, r = self.do(root.left), self.do(root.right)
        best = max(l[0], r[0], l[1] + r[1])
        new_height = 1 + max(l[1], r[1])
        return [best, new_height]
