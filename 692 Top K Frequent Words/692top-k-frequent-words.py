from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = Counter(words)
        q = []
        heapq.heapify(q)

        for i in d:
            heapq.heappush(q, (-1 * d[i], i))
        
        ls = []

        while (k > 0):
            count, s = heapq.heappop(q)
            ls.append(s)
            k -= 1
        
        return ls