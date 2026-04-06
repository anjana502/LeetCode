class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {0: 0, 1: 1, 2: -1, 3: -1, 4: -1, 5: -1, 6: 9, 7: -1, 8: 8, 9: 6}
        n = int(num)
        m = 0
        
        while (n != 0):
            r = n % 10
            
            if (d[r] == -1):
                return False
            
            m = m * 10 + d[r]
            n //= 10
        
        if (int(num) == m):
            return True
        return False