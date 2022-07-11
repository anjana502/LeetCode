from collections import deque
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n = len(grid2)
        m = len(grid2[0])
        s = set()
        ls = []
        
        def islands(i, j):
            q = deque()
            q.append((i, j))
            s.add((i, j))
            p = []
            d = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            while (len(q) != 0):
                r, c = q.popleft()
                p.append([r, c])
                for k, g in d:
                    row = r + k
                    col = c + g
                    if ((row < 0 or row >= n) or (col < 0 or col >= m) or ((row, col) in s) or grid2[row][col] != 1):
                        continue
                    q.append((row, col))
                    s.add((row, col))
            ls.append(p)
            
        for i in range(n):
            for j in range(m):
                if (grid2[i][j] == 1 and (i, j) not in s):
                    islands(i, j)
        
        count = 0
        for i in ls:
            flag = False
            for j, k in i:
                if (grid1[j][k] == 0):
                    flag = True
                    break
            if (flag == False):
                count += 1
        
        return count