class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        i = 0
        while (True):
            if (part in s):
                i = s.index(part)
                s = s[:i] + s[i+len(part):]
                i = 0
            else:
                break
        return s
        