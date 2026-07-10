# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''

        0 -> 1 -> 2 -> 3 -> null 
 prev head
        1 -> 0 -> null
        curr prev 

        things to keep track of
        1. keep track of my curr node
        2. next node 
        3. prev node (so i don't lose the whole list)

        # null ==  none in python
        '''
        prev, curr = None, head

        while curr: 
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp
        return prev 
        
        # Time O(n) - for every element, i just go through the elements once
        # Memory O(1) - just using pointers
