class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # want to find the most frequent elements by order k
        # return the k most frequent elements in the array
        # if k=2 and in the array 2 is there twice and 3 is there three times, those are the top 2 k elements
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # add the nnumbers to a freq map, return the k highest frequencies
        arr = []
        for num, count in freq.items(): 
            arr.append([count, num])
        arr.sort() # sort array by least to greatest freq

        result = []
        while len(result) < k: 
            result.append(arr.pop()[1]) # to get the "most" freq, pop from the end of the list. stop when i reach k amount of elements in result 

        return result        




























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

        