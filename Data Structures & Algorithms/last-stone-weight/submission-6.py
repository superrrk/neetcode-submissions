class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # find the two heaviest stones
        # 1. equal weights, destroy the stones and delete them from arr
        # 2. destroy the lighter weight stone,
        # and subtract the lighter stone's weight from the heavier stone's weight
        # stop when there's 1 or less stones
        # return the weight of the last stone/0 if none left

        # [2, 3, 6, 2, 4]
        #         |     |
        # 4 < 6? yes --> 6 - 4 = 2
        # [2, 3, 2, 2]
        #  |  |
        # 2 < 3? yes --> 3 - 2 = 1
        # [1, 2, 2]
        # |   | 
        # 2 == 2? 
        # [1]
        # return 1

        # plan: max heap - to find the two heaviest stones
        # stop destroying stones once the arr <= 1

        # max heap implementation 
        # stones = [-s for s in stones]

        # o(1): space complexity 
        # reverse the stones list to create the max heap by converting all stone values
        # to negative, this way -8 would be the largest by minheap
        for i in range(len(stones)):
            stones[i] = -stones[i]

        # o(n): heapify operation
        heapq.heapify(stones)

        # stop simulation after 1 stones
        while len(stones) > 1:
            first = heapq.heappop(stones) # largest 
            second = heapq.heappop(stones) # 2nd largest
            if second > first: 
                heapq.heappush(stones, first - second)
        
        # adds a 0 stone to the end of list, incase there's none left
        stones.append(0)
        return abs(stones[0])

        # time: o(n log n)
        # space: o(n) w/ line 26 implementation 


        
