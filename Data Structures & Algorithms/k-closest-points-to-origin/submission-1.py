class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # k - # of points found 
        # array, x and y coords on a plane
        # i want to find the number of points closests to the origin
        # using euclidean distrance 

        # create a minHeap to store the smallest distances
        # this way, i can pop k amount of points
        # in ascending order

        minHeap = []
        for x, y in points: 
            # find the distance
            distance = (x**2) + (y**2)
            minHeap.append([distance, x, y])
        
        heapq.heapify(minHeap)
        result = []
        while k > 0: 
            distance, x, y = heapq.heappop(minHeap)
            result.append([x, y])
            k -= 1
        
        return result
