class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ls = s.split(" ")

        if (len(pattern) != len(ls)):
            return False
        
        d = {}
        s1 = set()

        for i in range(len(pattern)):
            if (pattern[i] not in d):
                if (ls[i] in s1):
                    return False
                
                d[pattern[i]] = ls[i]
                s1.add(ls[i])
            elif (d[pattern[i]] != ls[i]):
                return False

        return True