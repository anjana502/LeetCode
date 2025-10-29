class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        s1 = {"a", "e", "i", "o", "u"}
        i = 0
        j = len(s) - 1

        while (i < j):
            if (s[i].lower() in s1 and s[j].lower() in s1):
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            if (s[i].lower() not in s1):
                i += 1
            if (s[j].lower() not in s1):
                j -= 1
        
        s = "".join(s)
        
        return s