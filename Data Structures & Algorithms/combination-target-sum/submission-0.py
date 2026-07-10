class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # use same number many times
        # a combination is the same if the freq of each number is the same

        # 2 + 2 + 5 = 9 
        # 9 

        # use backtracking to explore all possible choices
        result = []

        # i - which candidate we are allowed to choose 
        # cur = list of what values we can add to the cur combination
        # total = total sum to compare to target sum
        def dfs(i, cur, total):
            # found result
            if total == target: 
                result.append(cur.copy()) # create a copy 
                return 
            # out of bounds, or total higher than target
            if i >= len(nums) or total > target: 
                return 

            # include the candidate 
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # don't include any occurences of i
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return result
            
