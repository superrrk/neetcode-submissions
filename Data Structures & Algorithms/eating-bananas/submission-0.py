class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r # max our solution can be

        while l <= r: 
            k = (l + r) // 2
            hours = 0 
            for p in piles: 
                hours += math.ceil(p / k)

            if hours <= h: 
                result = min(result, k)
                r = k - 1 # search the left portion, find a lower rate
            else: 
                l = k + 1 # search the right portion, find a bigger rate

        return result