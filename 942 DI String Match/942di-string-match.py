class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ls = [i for i in range(len(s) + 1)]
        i = 0
        
        def reverse(start, end):
            while (start < end):
                ls[start], ls[end] = ls[end], ls[start]
                start += 1
                end -= 1
        
        while (i < len(s)):
            if (s[i] == "I"):
                i += 1
            else:
                count = 0
                start = i
                
                while (i < len(s) and s[i] == "D"):
                    count += 1
                    i += 1
                
                end = i
                
                reverse(start, end)
        
        return ls