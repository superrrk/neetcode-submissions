class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # target not in nums --> - 1
        # target found --> index

        # array empty? --> no, at least 1 number

        # bst 
        # [ -1, 0, 2, 4, 6, 8]
        # [ l                r]
        # 0 + 5 // 2 = 2 
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2) # middle index
            
            if nums[mid] < target: 
                l = mid + 1
            
            elif nums[mid] > target:
                r = mid - 1

            else: 
                return mid
                
        return -1


            

