from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        s = set()
        n = len(grid)
        m = len(grid[0])
        ls = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        count = 0

        for i in range(n):
            for j in range(m):
                if (grid[i][j] == 2):
                    q.append((i, j))
                    s.add((i, j))
                elif (grid[i][j] == 1):
                    fresh += 1
        
        while (fresh != 0 and len(q) != 0):
            d = len(q)

            for l in range(d):
                i, j = q.popleft()

                for k in ls:
                    row = i + k[0]
                    col = j + k[1]

                    if ((row < 0 or row >= n) or (col < 0 or col >= m) or ((row, col) in s) or (grid[row][col] != 1)):
                        continue
                    
                    q.append((row, col))
                    s.add((row, col))
                    fresh -= 1
            
            count += 1
        
        if (fresh == 0):
            return count
        return -1