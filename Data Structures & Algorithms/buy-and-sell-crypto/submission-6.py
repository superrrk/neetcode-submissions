class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window technique, move the l pointer to the r if l price is greater
        # want to buy low, otherwise increase right pointer to find max profit

        l, r = 0, 1
        max_profit = 0

        while r < len(prices): 
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else: 
                l = r
            r += 1
        
        return max_profit