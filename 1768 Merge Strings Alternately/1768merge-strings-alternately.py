class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        i = 0
        j = 0
        flag = True

        while (i < len(word1) and j < len(word2)):
            if (flag == True):
                s += word1[i]
                i += 1
            else:
                s += word2[j]
                j += 1
            
            flag = not (flag)
        
        if (i < len(word1)):
            s += word1[i:]
        if (j < len(word2)):
            s += word2[j:]
        
        return s