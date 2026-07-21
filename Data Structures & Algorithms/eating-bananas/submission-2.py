class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # want to find eating rate of r 
        # time to eat each pile must be less than h
        # each pile can be eaten at a rate of >= 1 bananas/hr
        # use binary search to find the min eating rate

        l, r = 1, max(piles)
        res = r

        while l <= r: 
            k = (l + r) // 2
            totalTime = 0 

            for p in piles: 
                totalTime += math.ceil(float(p) / k)

            if totalTime <= h: 
                res = k 
                r = k - 1
            else: 
                l = k + 1
        return res 

        

