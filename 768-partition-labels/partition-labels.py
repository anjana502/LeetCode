class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}

        for i in range(len(s)):
            d[s[i]] = i
        
        start = 0
        ls = []
        max1 = d[s[0]]

        for i in range(1, len(s)):
            if (i > max1):
                ls.append(i - start)
                start = i
            
            max1 = max(max1, d[s[i]])
        
        ls.append(i - start + 1)

        return ls