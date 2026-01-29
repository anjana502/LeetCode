class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        row = n - 1
        col = 0
        count = 0

        while (row >= 0 and col < m):
            if (grid[row][col] < 0):
                count += (m - col)
                row -= 1
            else:
                col += 1
        
        return count