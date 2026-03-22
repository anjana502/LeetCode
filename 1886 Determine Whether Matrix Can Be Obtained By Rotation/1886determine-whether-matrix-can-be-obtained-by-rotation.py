class Solution:
    def rotateMatrix(self, mat):
        for i in range(len(mat)):
            for j in range(i + 1, len(mat)):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
        for i in range(len(mat)):
            mat[i].reverse()
        
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(3):
            if (mat == target):
                return True
            
            self.rotateMatrix(mat)
        
        if (mat == target):
            return True
        return False 