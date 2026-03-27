class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat)
        m = len(mat[0])
        k %= m

        for i in range(n):
            if (i % 2 == 0):
                ls = mat[i][k:] + mat[i][:k]
            else:
                ls = mat[i][k:] + mat[i][:k]

            print(ls)

            if (ls != mat[i]):
                return False
        
        return True
                