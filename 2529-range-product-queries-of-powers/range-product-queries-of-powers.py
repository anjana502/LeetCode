from math import log

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ls = []

        while (n != 0):
            p = pow(2, int(log(n, 2)))
            ls.append(p)
            n -= p
        
        ls = ls[::-1]

        for i in range(1, len(ls)):
            ls[i] *= ls[i - 1]
        
        ls1 = []

        for i, j in queries:
            if (i == 0):
                ls1.append(ls[j] % (10 ** 9 + 7))
            else:
                ls1.append((ls[j] // ls[i - 1]) % (10 ** 9 + 7))
        
        return ls1