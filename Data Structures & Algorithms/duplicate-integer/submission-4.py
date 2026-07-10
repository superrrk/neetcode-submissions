class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        given an input of integers, i want to return true if there's
        more than one instance of a number, this means there's a 
        duplicate. otherwise, return false

        ex: [1, 2, 3, 3]
        
        seen = {1, 2, 3}
                      ^ SEEN ALR

        i add every int to the set, and 
        if a number is already seen in the set, 
        then we found a duplicate

        Time: O(n)
        - python's set is implemented as a hash table
        - i only scan through the list once, and each lookup
        and inseration into a hash set takes constatnt time on average
        O(n) * (O(1) + O(1)) = O(n)
        Space: O(n)
        - in the worst case, i would need to store every
        number into the set, in the case that there 
        are no duplicates, stores up to n elements in set
        '''

        # use a set to keep track of what numbers appear
        seen = set()
        # for every number, check if it's already in the set
        # if it is, then return True
        # if it's not, add it to the set
        for digit in nums:
            if digit in seen:
                return True
            seen.add(digit)
        # return False because you haven't seen a duplicate 
        # and you're at the end of your input array
        return False
        