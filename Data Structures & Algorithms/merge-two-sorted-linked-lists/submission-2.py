# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        need to compare two lists
        compare the values of list 1 and 2
        if list 1 < 2 then we add list 1, and remove what we added
        else: we add list 2 and remove what we added

        keep going until no more lists

        while l1 and l2:
            list 1 and list 2 comparing

        if l2:
            add all of list2
        else:
            add all of list1

        '''
        dummy = ListNode()
        tail = dummy

        if list1 is None:
            return list2
        
        if list2 is None: 
            return list1


        while list1 and list2: 
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 or list2

        return dummy.next
        

        