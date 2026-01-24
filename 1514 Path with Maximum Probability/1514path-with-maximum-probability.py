import heapq

class Solution:    
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for i in range(n)]
        q = []
        heapq.heapify(q)
        ls = [0.0 for i in range(n)]
        ls[start_node] = 1
        heapq.heappush(q, (-1 * ls[start_node], start_node))

        for i in range(len(edges)):
            adj[edges[i][0]].append((edges[i][1], succProb[i]))
            adj[edges[i][1]].append((edges[i][0], succProb[i]))
        
        while (len(q) != 0):
            w, u = heapq.heappop(q)
            w *= -1

            for v, d in adj[u]:
                if (ls[v] < w * d):
                    ls[v] = w * d
                    heapq.heappush(q, (-1 * ls[v], v))
        
        return ls[end_node]