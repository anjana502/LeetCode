class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        s = "".join([i for i in start if i != "X"])
        t = "".join([j for j in result if j != "X"])

        if (s != t):
            return False
        
        j = 0

        for i in range(len(start)):
            if (start[i] == "L"):
                while (j < len(result) and result[j] != "L"):
                    j += 1
                
                if (j > i):
                    return False
                
                j += 1
        
        j = 0

        for i in range(len(start)):
            if (start[i] == "R"):
                while (j < len(result) and result[j] != "R"):
                    j += 1
                
                if (j < i):
                    return False
                
                j += 1
        
        return True