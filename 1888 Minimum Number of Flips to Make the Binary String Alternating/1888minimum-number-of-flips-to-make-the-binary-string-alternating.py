class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        alt1 = ""
        alt2 = ""

        for i in range(len(s)):
            alt1 += "0" if (i % 2 == 0) else "1"
            alt2 += "1" if (i % 2 == 0) else "0"
        
        d1 = 0
        d2 = 0
        j = 0
        min1 = float("inf")

        for i in range(len(s)):
            if (s[i] != alt1[i]):
                d1 += 1
            if (s[i] != alt2[i]):
                d2 += 1
            
            while ((i - j + 1) > n):
                if (s[j] != alt1[j]):
                    d1 -= 1
                if (s[j] != alt2[j]):
                    d2 -= 1
                
                j += 1
            
            if ((i - j + 1) == n):
                min1 = min(min1, d1, d2)
        
        return min1