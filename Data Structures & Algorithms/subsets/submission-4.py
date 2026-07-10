class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # subset - unique, no duplicates or "permutations" allowed
        # implement back tracking
        result = []
        subset = []
        # [1, 2, 3]
        # 0   1   2

        def dfs(i):
            # i - which element we are visiting
            # out of bounds
            if i >= len(nums):
                result.append(subset.copy()) # we add the leaf node
                return
            
            # include nums[i] - left decision 
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1) 
        
        dfs(0)
        return result
            

