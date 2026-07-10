class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        # looking through speeds [1, 2, 3,..., h]
        result = r # max our solution can be

        while l <= r: 
            k = (l + r) // 2 # mid point 
            hours = 0 

            # find how many hours it takes to eat one pile
            for p in piles: 
                hours += math.ceil(p / k)

            # check if my hours are less than my hour limit h 
            if hours <= h: 
                result = min(result, k)
                r = k - 1 # search the left portion, find a lower rate
            else: 
                l = k + 1 # search the right portion, find a bigger rate

        return result