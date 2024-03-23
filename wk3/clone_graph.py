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
      
        stack = [node]
        visited = set()
        new_nodes = {}
       

        while stack:
            e = stack.pop()
            if e.val in new_nodes:
                new_e = new_nodes[e.val]
            else:
                new_e = Node(e.val, [])
            

           
            if e not in visited:
                visited.add(e)
                for n in e.neighbors:
                    if not n.val in new_nodes:
                        new_nodes[n.val] = Node(n.val, [])
                    new_e.neighbors.append(new_nodes[n.val])
                    stack.append(n)
    
                   
           
           
       
        return new_nodes[1]