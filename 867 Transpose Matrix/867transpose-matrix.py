class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        mat = [[0 for j in range(n)] for i in range(m)]

        for i in range(n):
            for j in range(m):
                mat[j][i] = matrix[i][j]
        
        return mat