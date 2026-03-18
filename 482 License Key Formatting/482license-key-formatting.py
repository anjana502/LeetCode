class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = "".join(s.split("-"))
        n = len(s)
        s1 = ""
        i = len(s) - 1
        
        while (i >= 0):
            if ((i - k + 1) >= 0):
                s2 = s[i - k + 1: i + 1]
            else:
                s2 = s[:i + 1]
            
            s1 = s2.upper() + "-" + s1
            i -= k
        
        s1 = s1[:-1]
        
        return s1