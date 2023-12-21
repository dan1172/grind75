# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#     if list1 is None:
#         return list2
#     if list2 is None:
#         return list1
    
#     if list1.val > list2.val:
#         head = ListNode(list2.val, None)
#         list2 = list2.next
#     else:
#         head = ListNode(list1.val, None)
#         list1 = list1.next
#     tail = head
#     while (not list1 is None) and (not list2 is None):
#         if list1.val > list2.val:
#             # this means that list2 is smaller, so take from there
#             new_val = list2.val
#             list2 = list2.next
#         else:
#             # this means equal, or list1 is smaller, so take from list1
#             new_val = list1.val
#             list1 = list1.next
#         new_node = ListNode(new_val, None)
#         tail.next = new_node
#         tail = new_node
        
        
#     if list1 is None:
#         tail.next = list2
#     else:
#         tail.next = list1
#     return head

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dum = ListNode()
    while list1 and list2:
        if list1.val > list2.val:
            # this means that list2 is smaller, so take from there
            new_val = list2.val
            list2 = list2.next
        else:
            # this means equal, or list1 is smaller, so take from list1
            new_val = list1.val
            list1 = list1.next
        new_node = ListNode(new_val, None)
        tail.next = new_node
        tail = new_node
        
        
    if list1 is None:
        tail.next = list2
    else:
        tail.next = list1
    return dum.next