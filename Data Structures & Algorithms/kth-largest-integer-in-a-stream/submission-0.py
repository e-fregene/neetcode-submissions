class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.minHeap=nums
        
        heapq.heapify(self.minHeap) # Create Min heap O(n) to transform

        while len(self.minHeap) > self.k: #until len(heap)==k
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]