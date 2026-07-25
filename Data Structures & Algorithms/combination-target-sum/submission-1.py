class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # combination is unique if the freq of each number chosen is different
        # use backtracking to go through two options, 
            # add the num 
            # skip the num 
            
        result = []

        def dfs(i, currentList, total):
            
            if total == target: 
                result.append(currentList.copy())
                return
            if i >= len(nums) or total > target:
                return 
            
            # include nums[i]
            currentList.append(nums[i])
            dfs(i, currentList, total + nums[i])
            currentList.pop()  

            # skip nums[i]
            dfs(i + 1, currentList, total) 

        dfs(0, [], 0)
        return result
