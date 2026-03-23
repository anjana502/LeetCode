class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        n = len(name)
        m = len(typed)
        
        while (i < n and j < m):
            if (name[i] == typed[j]):
                i += 1
                j += 1
            else:
                while (j > 0 and j < len(typed) and typed[j] == typed[j - 1]):
                    j += 1
                
                if (i < n and j < m and name[i] != typed[j]):
                    return False
        
        while (j > 0 and j < len(typed) and typed[j] == typed[j - 1]):
            j += 1
            
        if (i == n and j == m):
            return True
        return False