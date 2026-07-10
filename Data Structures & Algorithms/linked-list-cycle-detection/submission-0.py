# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        '''
        1->2->3->4
           |     |
           |------
        
        1->2->3->4

        1->2->3->2



        check if there's a cycle
        
        set pointers: curr = head
        
        seen = set()

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False

        set(1, 2, 3, 4)






        '''


        curr = head
        seen = set()

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False



        