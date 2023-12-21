# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# We can probably use the fact that every node except for the first and last is 
# being found for a gcd for it twice
# So how do we find a prime decomposition 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head):
        