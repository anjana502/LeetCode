import heapq
from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        q = []
        heapq.heapify(q)
        n = len(barcodes)
        ls = [0 for i in range(n)]
        d = Counter(barcodes)
        i = 0

        for k in d:
            heapq.heappush(q, (-1 * d[k], k))
        
        while (len(q) != 0):
            count, d1 = heapq.heappop(q)
            count *= -1

            print((count, d1))

            while (count > 0):
                i = 1 if (i >= n) else i
                ls[i] = d1
                i += 2
                count -= 1
        
        return ls