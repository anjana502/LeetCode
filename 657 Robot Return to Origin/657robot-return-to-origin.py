class Solution:
    def judgeCircle(self, moves: str) -> bool:
        row = 0
        col = 0
        
        for i in moves:
            if (i == "U"):
                row -= 1
            elif (i == "D"):
                row += 1
            elif (i == "L"):
                col -= 1
            else:
                col += 1
        
        if ((row, col) == (0, 0)):
            return True
        return False