class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for i in range(n)]
        s = set()
        
        for u, v in edges:
            adj[u].append(v)
        
        @cache
        def dfs(node):
            if (node == destination):
                if (len(adj[node]) == 0):
                    return True
                return False
            if (node in s or len(adj[node]) == 0):
                return False
            
            s.add(node)
            
            for j in adj[node]:
                if (dfs(j) == False):
                    return False
            
            return True
        
        return dfs(source)