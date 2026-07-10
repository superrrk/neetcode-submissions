class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given an array, i want to return the integers that appear k times 
        # so i want to figure out how many times the number appears

        # [1,2,2,3,3,3] k = 2 
        # [2,3]
        
        freq = {}
        # 1. storing the frequency of each num in a hashmap
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        arr = []
        for num, cnt in freq.items():
            arr.append([cnt, num])
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
            # array is sorted by pairs, [freq, num]. arr is sorted ascending, from lowest
            # to greatest, so i must pop from the end of the list, to get the "most"
            # or highest frequency value 
            # i'll stop when i reach k amount of elements 
        return result

        # O(n log n) -> i'd have to go through each element 

        