class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open1 = 0
        close = 0
        s1 = ""
        prev = 0
        
        for i in range(len(s)):
            if (s[i] == "("):
                open1 += 1
            elif (s[i] == ")"):
                close += 1
            
            if (open1 == close):
                s1 += s[prev + 1: i]
                prev = i + 1
        
        return s1