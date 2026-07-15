class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # want to find two digits that equal the target
        # brute force: use nested for loop to track the sum of 2 digits
        # optimal: use a hashmap to store the differences and 
        # check if any number + the diff add up to the target

        seen = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [nums[index], nums[diff]]



























        seen = {}
        
        for i, num in enumerate(nums):
            diff = target - num 
            if diff in seen: 
                return [seen[diff], i]
            seen[num] = i





            


            

        

