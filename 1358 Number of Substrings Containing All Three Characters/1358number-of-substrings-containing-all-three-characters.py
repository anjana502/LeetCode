from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = defaultdict(lambda: 0)
        j = 0
        count = 0
        n = len(s)

        for i in range(len(s)):
            d[s[i]] += 1

            while (len(d) == 3):
                count += (n - i)
                d[s[j]] -= 1

                if (d[s[j]] == 0):
                    del d[s[j]]
                
                j += 1
        
        return count