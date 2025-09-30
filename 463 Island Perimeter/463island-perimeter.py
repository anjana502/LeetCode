class Solution:
    def bfs(self, i, j, grid, n, m):
        q = deque()
        q.append((i, j))
        s = set()
        s.add((i, j))
        count = 0
        ls = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while (len(q) != 0):
            d = q.popleft()

            for k in ls:
                row = d[0] + k[0]
                col = d[1] + k[1]

                if ((row < 0 or row >= n) or (col < 0 or col >= m) or (grid[row][col] != 1)):
                    count += 1
                    continue
                if ((row, col) in s):
                    continue
                
                q.append((row, col))
                s.add((row, col))
        
        return count

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if (grid[i][j] == 1):
                    return self.bfs(i, j, grid, n, m)