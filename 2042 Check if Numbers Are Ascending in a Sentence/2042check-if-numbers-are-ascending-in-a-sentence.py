class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        p = 0
        d = 0
        for i in s:
            if (i.isdigit() == True):
                d = d * 10 + int(i)
            else:
                if (p != 0):
                    if (d != 0 and d <= p):
                        return False
                if (d != 0):
                    p = d
                    d = 0
        if (p != 0):
            if (d != 0 and d <= p):
                return False
        return True