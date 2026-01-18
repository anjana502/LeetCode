import heapq

class Solution:
    def find(self, u, parent):
        if (u == parent[u]):
            return u
        
        parent[u] = self.find(parent[u], parent)
        
        return parent[u]
    
    def union(self, u, v, parent, rank):
        u_rep = self.find(u, parent)
        v_rep = self.find(v, parent)
        
        if (u_rep == v_rep):
            return False
        
        if (rank[u_rep] > rank[v_rep]):
            parent[v_rep] = u_rep
        elif (rank[v_rep] > rank[u_rep]):
            parent[u_rep] = v_rep
        else:
            parent[v_rep] = u_rep
            rank[u_rep] += 1
        
        return True
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        q = []
        heapq.heapify(q)
        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]

        for i in range(n - 1):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(q, (d, i, j))
        
        cost = 0
        count = 0
        
        while (len(q) != 0):
            d, i, j = heapq.heappop(q)
            
            if (self.union(i, j, parent, rank) == True):
                cost += d
                count += 1
            
            if (count == n - 1):
                break
        
        return cost