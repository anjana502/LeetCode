class Solution:
    def getHappyString1(self, i, n, ls, ls1):
        if (i == n):
            s = "".join(ls1)
            ls.append(s)
            return
        
        for char in "abc":
            if ((i == 0) or (i > 0 and ls1[i - 1] != char)):
                ls1[i] = char

                self.getHappyString1(i + 1, n, ls, ls1)
        
    def getHappyString(self, n: int, k: int) -> str:
        ls = []
        ls1 = ["" for i in range(n)]

        self.getHappyString1(0, n, ls, ls1)

        ls.sort()

        s = ls[k - 1] if (k - 1 < len(ls)) else ""

        return s