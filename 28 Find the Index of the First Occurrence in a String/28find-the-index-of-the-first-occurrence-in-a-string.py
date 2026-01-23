class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            j = 0

            while (j < m):
                if (needle[j] != haystack[i+j]):
                    break
                
                j += 1
            
            if (j == m):
                return i
        
        return -1