class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if (s1 == s2):
            return True
        
        ls = list(s1)

        if (s1[0] != s2[0]):
            ls[0], ls[2] = ls[2], ls[0]
            s1 = "".join(ls)

        if (s1 == s2):
            return True
        
        if (s1[1] != s2[1]):
            ls[1], ls[3] = ls[3], ls[1]
            s1 = "".join(ls)

        if (s1 == s2):
            return True
        return False