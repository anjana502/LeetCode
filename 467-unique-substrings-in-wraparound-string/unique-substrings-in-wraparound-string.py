class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        d = {i: 0 for i in "abcdefghijklmnopqrstuvwxyz"}
        n = len(s)

        for i in range(n):
            if  (i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or s[i] == "a" and s[i - 1] == "z")):
                curr += 1
            else:
                curr = 1
            
            d[s[i]] = max(d[s[i]], curr)

        count = sum(d.values())

        return count