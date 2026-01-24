class Solution:
    def numOfElements(self, matrix, n, mid):
        row = 0
        col = n - 1
        count = 0

        while (row < n and col >= 0):
            if (matrix[row][col] <= mid):
                count += col + 1
                row += 1
            else:
                col -= 1
        
        return count
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n-1][n-1]
        result = -1

        while (low <= high):
            mid = low + (high - low) // 2

            if (self.numOfElements(matrix, n, mid) < k):
                low = mid + 1
            else:
                result = mid
                high = mid - 1
        
        return result
                