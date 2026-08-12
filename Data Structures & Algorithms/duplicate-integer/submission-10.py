class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums: 
            if num in seen: 
                return True
            seen.add(num)
        return False

# add all the unique numbers in a set, if the number is already in the set, there is a duplicate. 
        