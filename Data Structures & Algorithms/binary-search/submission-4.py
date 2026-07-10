class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # time: O(log n)
        # space: O(1)
        l, r = 0, len(nums) - 1

        while l <= r:
            # avoid overflow 
            mid = l + ((r - l) // 2)
            # left of array 
            if nums[mid] > target:
                r = mid - 1
            # right of array 
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        # no result found
        return -1 

