# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if head == None: return False
        p1 = head
        p2 = head.next
        while p1 and p2:
            if p1 == p2: return True
            p1 = p1.next
            p2 = p2.next 
            if not p2:
                return False
            p2 = p2.next
        # if ever stop looping then there isnt a cycle
        return False
            