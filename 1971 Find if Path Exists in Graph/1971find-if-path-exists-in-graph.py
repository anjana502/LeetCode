class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for i in range(n)]

        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        
        s = set()

        def dfs(source, destination):
            if (source == destination):
                return True
            
            s.add(source)

            for j in adj[source]:
                if (j not in s):
                    if (dfs(j, destination) == True):
                        return True
            
            return False

        return dfs(source, destination)