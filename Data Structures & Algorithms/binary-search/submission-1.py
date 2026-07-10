class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            # check if middle is greater than target (move r to mid-1 to check left side of list)
            if nums[mid] > target: 
                r = mid - 1
            # check if middle is less than target (move l to mid+1 to check right side of list)
            elif nums[mid] < target: 
                l = mid + 1
            # otherwise it's the middle 
            else:
                return mid
        return -1