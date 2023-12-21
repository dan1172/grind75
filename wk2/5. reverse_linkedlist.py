# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head):
        last = None
        cur = head
        reversed_head = None
        while cur:
            new = ListNode(cur.val, None)
            if last == None:
                last = new
            else:
                new.next = last
                last  = new
            reversed_head = new
            cur = cur.next
        return reversed_head