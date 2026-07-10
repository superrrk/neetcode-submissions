class Solution:
    def findMin(self, nums: List[int]) -> int:
        # '''
        # [4, 5, 6, 1, 2, 3]
        # [3, 4, 5, 6, 7, 8]
        # '''
        result = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r: 
            # break the case for a sorted arr w/ no rotations
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            
            mid = (l + r) // 2
            result = min(result, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else: 
                r = mid - 1

        return result


