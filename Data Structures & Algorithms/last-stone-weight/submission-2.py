class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones) #its auto minheap, for max [-1] [-2]

        """
        if x=stones[-1] == y=stones[-2], detsoryed, pop both

        if x<y, x detsoryed, and y new weight is stones[y]-stones[x]

        """

        while len(stones) >1:
            y= heapq.heappop(stones) #biggest
            x=heapq.heappop(stones) #second
            
            heapq.heappush(stones, y-x)

        if len(stones) > 0:
            return abs(stones[0])
        else:
            return 0