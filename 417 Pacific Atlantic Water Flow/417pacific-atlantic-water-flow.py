from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        q1 = deque([])
        q2 = deque([])
        s1 = set()
        s2 = set()
        n = len(heights)
        m = len(heights[0])
        ls = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def bfs(q, s):
            while (len(q) != 0):
                d = q.popleft()

                for k in ls:
                    row = d[0] + k[0]
                    col = d[1] + k[1]

                    if ((row < 0 or row >= n) or (col < 0 or col >= m) or ((row, col) in s) or (heights[row][col] < heights[d[0]][d[1]])):
                        continue
                    
                    q.append((row, col))
                    s.add((row, col))
        
        for i in range(n):
            for j in range(m):
                if (i == 0 or j == 0):
                    q1.append((i, j))
                    s1.add((i, j))
                if (i == (n - 1) or j == (m - 1)):
                    q2.append((i, j))
                    s2.add((i, j))
        
        bfs(q1, s1)
        bfs(q2, s2)

        s1.intersection_update(s2)
        ls = []

        for i in s1:
            ls.append(list(i))
        
        return ls