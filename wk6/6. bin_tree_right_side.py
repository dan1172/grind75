# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        # thoughts --> can do a level order traversal that stores
        # the level and for each level return the one that was last seen
        
        # which is bfs that visits left first
        res = []
        stack = [(root, 0)]
        
        while stack:
            node, depth = stack.pop()
            if node is None:
                continue
            if len(res) < depth + 1:
                res.append(node.val)
            else:
                res[depth] = node.val
                
            stack.extend(((node.right, depth + 1), (node.left, depth + 1)))
            
        return res
        