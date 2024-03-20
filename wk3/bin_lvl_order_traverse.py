# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root ):
        q = [(root, 0)]
        res = []
        temp = []
        level = 0
        while q:
            cur, l = q.pop(0)
            if (cur is None) :
                continue
            
            if l == level:
                temp.append(cur.val)
            else:
                level = l
                res.append(temp)
                temp = [cur.val]
            q.extend(((cur.left, l + 1), ( cur.right, l + 1)))
        if len(temp) != 0:
            res.append(temp)
        return res
        