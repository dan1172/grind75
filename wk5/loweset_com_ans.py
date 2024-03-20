# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        
        # find path from root to p and root to q
        prev = {}
        stack = [root]
        prev[root] = None
        while stack:
            cur = stack.pop()
            if cur is None:
                continue
            if cur.left is not None:
                prev[cur.left] = cur
                stack.append(cur.left)
            if cur.right is not None:
                prev[cur.right] = cur
                stack.append(cur.right)
        
        pl = [p]
        cur = prev[p]
        while cur is not None:
            pl.append(cur)
            cur = prev[cur]
            
        ql = [q]
        cur = prev[q]
        while cur is not None:
            ql.append(cur)
            cur = prev[cur]
            
        for node in ql:
            if node in pl:
                return node
        
        # compare paths
        return None