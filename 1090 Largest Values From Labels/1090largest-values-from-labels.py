from collections import defaultdict

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        ls = list(sorted(zip(values, labels), key = lambda i: -1 * i[0]))
        d = defaultdict(lambda: 0)
        n = 0
        i = 0
        val = 0
        
        while (i < len(ls) and n < numWanted):
            if (d[ls[i][1]] < useLimit):
                val += ls[i][0]
                d[ls[i][1]] += 1
                n += 1
            i += 1
        
        return val