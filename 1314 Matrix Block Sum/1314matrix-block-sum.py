class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        
        for i in range(n):
            for j in range(m):
                if (i - 1 >= 0):
                    mat[i][j] += mat[i-1][j]
                if (j - 1 >= 0):
                    mat[i][j] += mat[i][j-1]
                if ((i - 1 >= 0) and (j - 1 >= 0)):
                    mat[i][j] -= mat[i-1][j-1]
        
        ls = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                min_row = max(0, i - k)
                max_row = min(i + k, n - 1)
                min_col = max(0, j - k)
                max_col = min(j + k, m - 1)
                
                ls[i][j] = mat[max_row][max_col]
                
                if (min_row - 1 >= 0):
                    ls[i][j] -= mat[min_row - 1][max_col]
                if (min_col - 1 >= 0):
                    ls[i][j] -= mat[max_row][min_col - 1]
                if ((min_row - 1 >= 0) and (min_col - 1 >= 0)):
                    ls[i][j] += mat[min_row - 1][min_col - 1]
        
        return ls