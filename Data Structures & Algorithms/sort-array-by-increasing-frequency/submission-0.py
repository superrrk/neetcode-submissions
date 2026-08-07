class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # frequencys stored in count 
        # 1 : 2
        # 2: 3
        # 3 : 1
        count = Counter(nums)
        nums.sort(key=lambda n: (count[n], -n))
        return nums
