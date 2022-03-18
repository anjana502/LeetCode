class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ls = []
        ls.append(-1)
        if (s == ""):
            return 0
        max1 = 0
        for i in range(len(s)):
            if (s[i] == '('):
                ls.append(i)
            else:
                if (len(ls) != 0):
                    ls.pop()
                if (len(ls) != 0):
                    max1 = max(max1, i - ls[-1])
                    
                else:
                    ls.append(i)
        return max1