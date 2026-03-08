class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s1 = s + s
        
        if (s in s1[1:-1]):
            return True
        return False