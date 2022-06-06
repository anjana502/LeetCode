class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0 for j in range(n)] for i in range(n)]
        d = 0
        t = 0
        b = n - 1
        l = 0
        r = n - 1
        p = 1
        
        while (t <= b and l <= r):
            if (d == 0):
                for i in range(l, r + 1):
                    m[t][i] = p
                    p += 1
                t += 1
            elif (d == 1):
                for i in range(t, b + 1):
                    m[i][r] = p
                    p += 1
                r -= 1
            elif (d == 2):
                for i in range(r, l - 1, -1):
                    m[b][i] = p
                    p += 1
                b -= 1
            else:
                for i in range(b, t - 1, -1):
                    m[i][l] = p
                    p += 1
                l += 1
            d = (d + 1) % 4
        return m