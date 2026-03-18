import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        q = []
        heapq.heapify(q)

        for i in d:
            heapq.heappush(q, (d[i], i))

            if (len(q) > k):
                heapq.heappop(q)
        
        ls = []
        
        while (len(q) != 0):
            count, d = heapq.heappop(q)
            ls.append(d)
        
        return ls