import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n + 1)]

        for i in times:
            adj[i[0]].append((i[1], i[2]))

        q = []
        heapq.heapify(q)
        ls = [float("inf") for i in range(n + 1)]
        ls[k] = 0
        heapq.heappush(q, (ls[k], k))

        while (len(q) != 0):
            d, u = heapq.heappop(q)

            for v, w in adj[u]:
                if (ls[v] > d + w):
                    ls[v] = d + w
                    heapq.heappush(q, (ls[v], v))
        
        max1 = max(ls[1:])

        if (max1 != float("inf")):
            return max1
        return -1