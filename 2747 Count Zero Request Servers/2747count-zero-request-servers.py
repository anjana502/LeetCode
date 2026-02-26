from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key = lambda i: i[1])
        d = defaultdict(lambda: 0)
        queries = [(queries[i], i) for i in range(len(queries))]
        queries.sort(key = lambda i: i[0])
        ls = [0 for i in range(len(queries))]
        j = 0
        k = 0

        for i in range(len(queries)):
            l = max(queries[i][0] - x, 1)
            r = queries[i][0]

            while (k < len(logs) and logs[k][1] <= r):
                d[logs[k][0]] += 1
                k += 1
            
            while (j < k and logs[j][1] < l):
                d[logs[j][0]] -= 1

                if (d[logs[j][0]] == 0):
                    del d[logs[j][0]]
                
                j += 1
            
            ls[queries[i][1]] = (n - len(d))
        
        return ls