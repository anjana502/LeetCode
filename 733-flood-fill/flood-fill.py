from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque([])
        s = set()
        n = len(image)
        m = len(image[0])
        ls = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def bfs(original_col):
            q.append((sr, sc, original_col))
            s.add((sr, sc))

            while (len(q) != 0):
                i, j, original_col = q.pop()
                image[i][j] = color

                for k in ls:
                    row = i + k[0]
                    col = j + k[1]

                    if ((row < 0 or row >= n) or (col < 0 or col >= m) or (image[row][col] != original_col) or ((row, col) in s)):
                        continue
                    
                    q.append((row, col, image[row][col]))
                    s.add((row, col))
        
        bfs(image[sr][sc])
        
        return image