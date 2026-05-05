class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        cost = 0
        row_diff = abs(startPos[0] - homePos[0])
        row = startPos[0]

        for i in range(row_diff):
            if (row < homePos[0]):
                row += 1
                cost += rowCosts[row]
            else:
                row -= 1
                cost += rowCosts[row]
        
        col_diff = abs(startPos[1] - homePos[1])
        col = startPos[1]

        for j in range(col_diff):
            if (col < homePos[1]):
                col += 1
                cost += colCosts[col]
            else:
                col -= 1
                cost += colCosts[col]
        
        return cost