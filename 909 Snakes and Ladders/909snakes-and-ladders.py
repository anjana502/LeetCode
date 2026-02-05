from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        ls = [0] * (n * n + 1)

        for i in range(n):
            for j in range(n):
                ls[(n - i - 1) * n + ((n - j) if ((n - i) % 2 == 0) else (j + 1))] = board[i][j]

        q = deque([])
        q.append(1)
        s = set()
        s.add(1)
        count = 1

        while (len(q) != 0):
            d = len(q)
            
            for i in range(d):
                pos = q.popleft()
                
                for k in range(pos + 1, min(pos + 6, n * n) + 1):
                    dest = ls[k] if (ls[k] != -1) else k

                    if (dest == n * n):
                        return count
                    
                    if (dest in s):
                        continue

                    q.append(dest)
                    s.add(dest)
            
            count += 1
        
        return -1