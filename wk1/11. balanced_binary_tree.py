# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        return self.do(root)[0]
    
    def do(self, root):  #[bool, int]
        # do the height stuff
        if root is None:
            return [True, 0]
        
        l_res, r_res = self.do(root.left), self.do(root.right)
        
        if root.val == 1:
            print(l_res[1],r_res[1] )
        return [l_res[0] and r_res[0] and abs(l_res[1] - r_res[1]) <= 1, 1 + max(l_res[1], r_res[1])]
           
        
        
# # soln from leetcode
# class Solution(object):
#     def isBalanced(self, root):
#         return (self.Height(root) >= 0)
#     def Height(self, root):
#         if root is None:  return 0
#         leftheight, rightheight = self.Height(root.left), self.Height(root.right)
#         if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
#         return max(leftheight, rightheight) + 1