from collections import Counter

class Solution:
    def beautySum1(self, s1):
        d = Counter(s1)
        max1 = max(d.values())
        min1 = min(d.values())
        d1 = max1 - min1

        return d1
    
    def beautySum(self, s: str) -> int:
        sum1 = 0

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                s1 = s[i:j]
                sum1 += self.beautySum1(s1)
        
        return sum1