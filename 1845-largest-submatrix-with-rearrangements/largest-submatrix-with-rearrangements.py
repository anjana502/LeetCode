class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        heights = [0 for j in range(m)]
        max1 = 0

        for i in range(n):
            for j in range(m):
                if (matrix[i][j] == 1):
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            ls = sorted(heights, reverse = True)

            for k in range(m):
                max1 = max(max1, ls[k] * (k + 1))

        return max1