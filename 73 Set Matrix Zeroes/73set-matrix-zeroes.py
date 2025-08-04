class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        flag = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] == 0):
                    matrix[i][0] = 0

                    if (j == 0):
                        flag = True
                    else:
                        matrix[0][j] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if (matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0
        
        if (matrix[0][0] == 0):
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if (flag == True):
            for i in range(len(matrix)):
                matrix[i][0] = 0     