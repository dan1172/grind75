# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def do(root, count) -> (int, int):
    if root == None:
        return 0
    l_num = do(root.left, count)
    r_num = do(root.right, count)
    count += abs(l_num - r_num)
    return l_num + r_num + root.val