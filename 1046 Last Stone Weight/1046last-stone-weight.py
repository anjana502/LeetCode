import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []
        heapq.heapify(q)

        for i in stones:
            heapq.heappush(q, -1 * i)

        while (len(q) > 1):
            x = -1 * heapq.heappop(q)
            y = -1 * heapq.heappop(q)

            if (x != y):
                x -= y
                heapq.heappush(q, -1 * x)
        
        if (len(q) != 0):
            return (-1 * q[0])
        return 0