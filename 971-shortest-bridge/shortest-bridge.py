class Solution:
    def dfs(self, i, j, n, grid, ls1, s):
        s.add((i, j))
        ls1.append((i, j))
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for k in d:
            row = i + k[0]
            col = j + k[1]

            if ((row < 0 or row >= n) or (col < 0 or col >= n) or ((row, col) in s) or (grid[row][col] != 1)):
                continue
            
            self.dfs(row, col, n, grid, ls1, s)
        
    def shortestBridge(self, grid: List[List[int]]) -> int:
        s = set()
        ls = []
        n = len(grid)

        for i in range(n):
            for j in range(n):
                if (grid[i][j] == 1 and (i, j) not in s):
                    ls1 = []

                    self.dfs(i, j, n, grid, ls1, s)

                    ls.append(ls1)
        
        min1 = float("inf")
        ls1 = ls[0]
        ls2 = ls[1]

        for r1, c1 in ls1:
            for r2, c2 in ls2:
                d = abs(r1 - r2) + abs(c1 - c2)
                min1 = min(min1, d - 1)
        
        return min1