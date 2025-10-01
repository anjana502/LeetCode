from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        in_degree = [0 for i in range(n)]

        for i in trust:
            adj[i[0] - 1].append(i[1] - 1)
            in_degree[i[1] - 1] += 1
        
        count = 0
        d = 0

        for i in range(n):
            if ((in_degree[i] == (n - 1)) and (len(adj[i]) == 0)):
                count += 1
                d = i + 1
        
        if (count != 1):
            return -1
        return d