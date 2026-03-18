class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for i in range(n)]
        ls = [0 for i in range(n)]

        for u, v in edges:
            adj[u].append((v, 1))
            adj[v].append((u, -1))
        
        def dfs(u, parent):
            for v, d in adj[u]:
                if (v != parent):
                    ls[0] += int(d < 0)
                    dfs(v, u)
        
        dfs(0, -1)

        def dfs1(u, parent):
            for v, d in adj[u]:
                if (v != parent):
                    ls[v] = ls[u] + d
                    dfs1(v, u)
        
        dfs1(0, -1)

        return ls