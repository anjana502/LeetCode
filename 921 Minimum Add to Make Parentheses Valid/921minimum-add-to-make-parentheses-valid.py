class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open1 = 0
        close = 0

        for i in s:
            if (i == "("):
                open1 += 1
            else:
                if (open1 > 0):
                    open1 -= 1
                else:
                    close += 1
        
        d = open1 + close

        return d