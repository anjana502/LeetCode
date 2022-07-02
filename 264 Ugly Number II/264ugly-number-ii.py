class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ls = []
        ls.append(1)
        i = 0
        j = 0
        k = 0
        p1 = 0
        p2 = 0
        p3 = 0
        while (len(ls) < n):
            p1 = ls[i] * 2
            p2 = ls[j] * 3
            p3 = ls[k] * 5
            min1 = min(p1, p2, p3)
            ls.append(min1)
            if (min1 == p1):
                i += 1
            if (min1 == p2):
                j += 1
            if (min1== p3):
                k += 1
        return ls[-1]