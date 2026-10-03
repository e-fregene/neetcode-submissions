class MedianFinder:

    def __init__(self):
        self.Heap = []
        heapq.heapify(self.Heap)

    def addNum(self, num: int) -> None:
        #simply add interger
        heapq.heappush(self.Heap, num)
        self.Heap.sort()

    def findMedian(self) -> float:
        if len(self.Heap) % 2 ==0:
            middle= len(self.Heap)//2
            sec_mid = middle-1

            median= self.Heap[middle] + self.Heap[sec_mid]
            return median/2

            #take two middle values average

        if len(self.Heap) % 2 !=0:
            middle= len(self.Heap)//2
            return self.Heap[middle]
        