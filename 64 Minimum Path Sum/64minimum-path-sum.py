class Solution:
    def minPathSum1(self, grid, mat, m, n):
        if (m == 0 or n == 0):
            mat[m][n] = 0
            return 0
        if (m == 1):
            mat[m][n] = grid[m - 1][n - 1] + self.minPathSum1(grid, mat, m, n - 1)
            return mat[m][n]
        if (n == 1):
            mat[m][n] = grid[m - 1][n - 1] +  self.minPathSum1(grid, mat, m - 1, n)
            return mat[m][n]
        
        if (mat[m][n] == False):
            mat[m][n] = grid[m - 1][n - 1] + min(self.minPathSum1(grid, mat, m - 1, n), self.minPathSum1(grid, mat, m, n - 1))
        
        return mat[m][n]
        
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mat = [[False for j in range(n + 1)] for i in range(m + 1)]

        result = self.minPathSum1(grid, mat, m, n)

        return result