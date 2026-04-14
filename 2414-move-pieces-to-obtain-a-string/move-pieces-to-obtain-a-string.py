class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        s = "".join([i for i in start if i != "_"])
        t = "".join([i for i in target if i != "_"])

        if (s != t):
            return False

        pos = 0

        for i in range(n):
            if (start[i] == "L"):
                while (pos < n and target[pos] != "L"):
                    pos += 1
                
                if ((pos == n) or (target[pos] == "L" and pos > i)):
                    return False
                
                pos += 1
        
        pos = n - 1

        for i in range(n - 1, -1, -1):
            if (start[i] == "R"):
                while (pos >= 0 and target[pos] != "R"):
                    pos -= 1
                
                if (pos < 0 or (target[pos] == "R" and pos < i)):
                    return False
                
                pos -= 1
        
        return True