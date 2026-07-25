class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = set()
        

        def generate_subsets(i, currList, total): 
            if total == target:
                result.add(tuple(currList)) # save sublist
                return
            
            #skip candidate
            if total > target or i == len(candidates): 
                return
            
            # add candidates[i]
            currList.append(candidates[i])
            generate_subsets(i + 1, currList, total + candidates[i])
            # do not add candidates[i]
            currList.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            generate_subsets(i + 1, currList, total)
    
        generate_subsets(0, [], 0)
        return [list(combination) for combination in result]


