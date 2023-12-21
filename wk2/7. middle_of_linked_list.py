# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        n = 0
        cur = head
        while cur:
            n = n + 1
            cur = cur.next
        print(f"total = {n}")
        if n % 2 == 1:
            n = n // 2 + 1
        else:
            n = (n // 2) + 1
        print(f"back down = {n}")
        rawr = 1
        meow = head
        print(f"meow value at beginnign {meow.val}")
        while rawr != n:
            meow = meow.next
            rawr = rawr + 1
        return meow