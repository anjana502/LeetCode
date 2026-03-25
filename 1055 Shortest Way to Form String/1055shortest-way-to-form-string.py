class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        n = len(source)
        m = len(target)
        count = 0
        j = 0

        def patternMatching(i, j):
            while (i < n and j < m):
                if (source[i] == target[j]):
                    j += 1
                i += 1
            
            return j
        
        while (j < m):
            index = patternMatching(0, j)

            if (index == j):
                return -1
            
            j = index
            count += 1
        
        return count