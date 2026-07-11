class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # want to check for the number of non-consecutive 0's, 
        # this is the # of flowers that can be placed
        # use greedy search to find the number of open spots

        if n == 0: 
            return True

        for i in range(len(flowerbed)): 
            if flowerbed[i] == 0:
                left_empty = i == 0 or flowerbed[i - 1] == 0
                right_empty = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1

                    if n == 0:
                        return True

        return False
