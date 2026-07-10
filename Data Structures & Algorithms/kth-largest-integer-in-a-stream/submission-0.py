class KthLargest:

    # stream - continually add numbers to list of numbers
    # include duplicates in order of "largest kth element"
    
    # in min heap, pop is O(log n) operation 

    def __init__(self, k: int, nums: List[int]):
        # create a minHeap with K largest integers
        self.minHeap, self.k = nums, k
        # turn array into a minHeap (sorted property)
        heapq.heapify(self.minHeap)
        # if there are more than k elements, 
        while len(self.minHeap) > k: 
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        
        # pop from the heap (when there's more than k elements)
        if len(self.minHeap) > self.k: 
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


