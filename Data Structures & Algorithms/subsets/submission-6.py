class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # want to find a subset combination 
        # use backtracking 
        result = []
        subset = []

        def dfs(i): 
            # i is for which element we are visiting
            if i >= len(nums): 
                result.append(subset.copy()) # add the leaf node
                return
            
            # include nums[i] - left decision, add the number
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i], don't add the number
            subset.pop()
            dfs(i + 1) 
        
        dfs(0)
        return result


            

