from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        q = []
        heapq.heapify(q)

        for i in d:
            heapq.heappush(q, (-1 * d[i], i))
        
        s = ""

        while (len(q) != 0):
            count, c = heapq.heappop(q)
            s += (-1 * count) * c
        
        return s