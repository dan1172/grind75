# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node):
       if node is None:
           return node
      
       stack = []
       visited = set()
       
       first_node = Node(node.val, [i for i in node.neighbors])

       while stack:
           e = stack.pop()
           if e in visited:
               continue
           
           
       
       return first_node