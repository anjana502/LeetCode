class Solution:
    def isSafe(self, s2):
        if ((int(s2[0]) == 0 and len(s2) > 1) or (int(s2) > 255)):
            return False
        return True

    def restoreIpAddresses1(self, i, s, ls, ls1, count):
        if (i == len(s)):
            if (count == 4):
                s1 = "".join(ls1)[:-1]

                ls.append(s1)
            return
        
        s2 = ""

        for j in range(i, len(s)):
            s2 += s[j]

            if (self.isSafe(s2) == True):
                ls1.append(s2)
                ls1.append(".")

                self.restoreIpAddresses1(j + 1, s, ls, ls1, count + 1)

                ls1.pop()
                ls1.pop()
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        s = list(s)
        ls = []
        ls1 = []

        self.restoreIpAddresses1(0, s, ls, ls1, 0)

        return ls 