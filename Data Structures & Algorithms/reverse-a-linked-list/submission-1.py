# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 
        # 
        prev, curr = None, head

        while curr: 
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp
        return prev 
        
        # Time O(n) - for every element, i just go through the elements once
        # Memory O(1) - just using pointers
