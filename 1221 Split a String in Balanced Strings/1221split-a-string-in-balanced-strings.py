class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        d = 0

        for i in s:
            if (i == "R"):
                d += 1
            else:
                d -= 1
            
            if (d == 0):
                count += 1
        
        return count