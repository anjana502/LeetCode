from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = deque([])
        adj = [[] for i in range(numCourses)]
        in_degree = [0 for i in range(numCourses)]
        ls = []

        for i in prerequisites:
            adj[i[1]].append(i[0])
            in_degree[i[0]] += 1
        
        for i in range(numCourses):
            if (in_degree[i] == 0):
                q.append(i)
        
        while (len(q) != 0):
            d = q.popleft()
            ls.append(d)

            for j in adj[d]:
                in_degree[j] -= 1

                if (in_degree[j] == 0):
                    q.append(j)
        
        if (len(ls) == numCourses):
            return ls
        return []