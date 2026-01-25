class Solution:
    def isSafe(self, row, col, board, n):
        for i in range(row - 1, -1, -1):
            if (board[i][col] == "Q"):
                return False
        
        for j in range(col - 1, -1, -1):
            if (board[row][j] == "Q"):
                return False
        
        i = row - 1
        j = col - 1

        while (i >= 0 and j >= 0):
            if (board[i][j] == "Q"):
                return False
            
            i -= 1
            j -= 1
        
        i = row - 1
        j = col + 1

        while (i >= 0 and j < n):
            if (board[i][j] == "Q"):
                return False
            
            i -= 1
            j += 1
        
        return True
    
    def totalNQueens1(self, row, board, n, s):
        if (row == n):
            s1 = ""

            for i in board:
                s2 = "".join(i)
                s1 += s2
            
            s.add(s1)
            return
        
        for col in range(n):
            if (self.isSafe(row, col, board, n) == True):
                board[row][col] = "Q"
                self.totalNQueens1(row + 1, board, n, s)
                board[row][col] = "."
        
    def totalNQueens(self, n: int) -> int:
        board = [["." for j in range(n)] for i in range(n)]
        s = set()

        self.totalNQueens1(0, board, n, s)

        return len(s)