class Solution:
    def minPathSum1(self, n, m, mat, grid):
        if (n == 0 or m == 0):
            return 0
        if (mat[n][m] != float("inf")):
            return mat[n][m]
        if (n == 1):
            mat[n][m] = grid[n - 1][m - 1] + self.minPathSum1(n, m - 1, mat, grid)
            return mat[n][m]
        if (m == 1):
            mat[n][m] = grid[n - 1][m - 1] + self.minPathSum1(n - 1, m, mat, grid)
            return mat[n][m]
        
        mat[n][m] = grid[n - 1][m - 1] + min(self.minPathSum1(n - 1, m, mat, grid), self.minPathSum1(n, m - 1, mat, grid))

        return mat[n][m]
        
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        mat = [[float("inf") for j in range(m + 1)] for i in range(n + 1)]

        self.minPathSum1(n, m, mat, grid)

        print(mat)
        
        return mat[n][m]