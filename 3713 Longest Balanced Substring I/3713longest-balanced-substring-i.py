from collections import defaultdict

class Solution:
    def longestBalanced(self, s: str) -> int:
        result = -1

        for i in range(len(s)):
            d = defaultdict(lambda: 0)

            for j in range(i, len(s)):
                d[s[j]] += 1
                max1 = max(d.values())
                min1 = min(d.values())

                if (max1 == min1):
                    result = max(result, (j - i + 1))
        
        return result