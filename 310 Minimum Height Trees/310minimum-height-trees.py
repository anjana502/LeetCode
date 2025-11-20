from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if (len(edges) == 0):
            return [0]

        adj = [[] for i in range(n)]
        in_degree = [0 for i in range(n)]

        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
            in_degree[i[0]] += 1
            in_degree[i[1]] += 1
        
        q = deque([])

        for i in range(len(in_degree)):
            if (in_degree[i] == 1):
                q.append(i)
        
        while (len(q) != 0):
            d = len(q)
            ls = []

            for i in range(d):
                node = q.popleft()
                ls.append(node)

                for j in adj[node]:
                    in_degree[j] -= 1

                    if (in_degree[j] == 1):
                        q.append(j)
        
        return ls