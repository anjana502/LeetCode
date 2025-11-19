class Solution:
    def uniquePaths1(self, m, n, mat):
        if (m == 1 or n == 1):
            return 1
        
        if (mat[m][n] == 0):
            mat[m][n] = self.uniquePaths1(m - 1, n, mat) + self.uniquePaths1(m, n - 1, mat)

        return mat[m][n]

    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[0 for i in range(n + 1)] for j in range(m + 1)]

        return self.uniquePaths1(m, n, mat)