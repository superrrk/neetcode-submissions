class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''

        - BRUTE FORCE: use same direction two pointers to add up two ints (i, j)
        and if they equal to 'target' 
        - Optimal: use a hashmap and pass through it once, seeing if the 
        difference from the target and the curr num, is in the seen 
        set (hashmap)

        time: O(n)
        space: O(n)

        '''

        seenMap = {}
        
        # key = indices 
        # values = numbers
        for i, n in enumerate(nums):
            diff = target - n
            # return the indices if the difference has been seen
            if diff in seenMap: 
                return [seenMap[diff], i]
            # no match yet, so store the number in seen
            seenMap[n] = i




