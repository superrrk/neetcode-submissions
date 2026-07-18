# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # idea is to flip all the next to prev
        # store curr.next in temp var
        # set next to prev
        # set prev to curr
        # set curr to temp var
        # return prev

        prev, curr = None, head

        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
        
