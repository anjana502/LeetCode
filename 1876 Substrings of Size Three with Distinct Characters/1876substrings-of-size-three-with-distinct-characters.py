from collections import defaultdict

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        d = defaultdict(lambda: 0)
        count = 0
        j = 0

        for i in range(len(s)):
            d[s[i]] += 1

            while (((i - j + 1) > 3) or (d[s[i]] > 1)):
                d[s[j]] -= 1
                j += 1
            
            if (((i - j + 1) == 3) and (d[s[i]] == 1)):
                count += 1
        
        return count