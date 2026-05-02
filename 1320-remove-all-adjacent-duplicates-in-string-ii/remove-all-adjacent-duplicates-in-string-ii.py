class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for i in range(len(s)):
            if (len(stack) != 0 and s[i] == stack[-1][0]):
                stack[-1][1] += 1

                if (stack[-1][1] == k):
                    stack.pop()
            else:
                stack.append([s[i], 1])
        
        s1 = ""

        for char, d in stack:
            s1 = s1 + (d * char)
        
        return s1