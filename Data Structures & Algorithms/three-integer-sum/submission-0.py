class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # array empty? - no 
        # [ -1 , 0 , 1 ] 

        # sort through my array
        # nums[i] + nums[j] + nums[k]

        # [-1, -1, 0, 1, 2, 4]
        #  a     l           r 
        #         b           c 
        # -1 + 
        # -a = l + r and get 0 

        result = [] # store indices
        nums.sort()

        for i, a in enumerate(nums):
           # edge case: can't find indices that will equal 0
            if a > 0:
                break

            # skip duplicates 
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result

