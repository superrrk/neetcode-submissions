class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # want to find two digits that equal the target
        # brute force: use nested for loop to track the sum of 2 digits
        # optimal: use a hashmap to store the differences and 
        # check if any number + the diff add up to the target

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []







            


            

        

