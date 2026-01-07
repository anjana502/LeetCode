import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = []
        heapq.heapify(q)
        gap = float("inf")
        idle = float("inf")
        d = Counter(tasks)

        for i in d:
            heapq.heappush(q, -1 * d[i])
        
        while (len(q) != 0):
            d1 = -1 * heapq.heappop(q)

            if (gap == float("inf")):
                gap = d1 - 1
                idle = gap * n
            else:
                min1 = min(gap, d1)
                idle -= min1
        
        d2 = len(tasks)
        
        if (idle > 0):
            d2 += idle

        return d2 