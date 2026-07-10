class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # edge cases: no empty arr
        
        # [ 3, 4, 5, 6]
        # 7 - 3 = 4
        # 
        # hashmap 
        seen = {} # value : index
        # 3 : 0 

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen: 
                return [seen[diff], i]
            seen[num] = i
        
    # time o(n)
    # space o(n)





            


            

        

