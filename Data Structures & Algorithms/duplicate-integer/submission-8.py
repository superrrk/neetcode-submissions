class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # want to find an array with all unique numbers
        # use a set to keep track of numbers already seen
        # if a number is seen before, then return true

        seen = set()

        for num in nums:
            if num in seen: 
                return True
            seen.add(num)
        return False


        