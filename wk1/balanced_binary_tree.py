# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        # make sure left and right tree is balanced asw
        return self.isBalanced(root.right) and self.isBalanced(root.left)