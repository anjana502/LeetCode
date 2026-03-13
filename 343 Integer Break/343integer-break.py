class Solution:
    def integerBreak1(self, k, n, count, p, ls):
        if (n == 0):
            if (count >= 2):
                ls[0] = max(ls[0], p)
            return
        if (n < 0 or k > n):
            return

        self.integerBreak1(k, n - k, count + 1, p * k, ls)

        self.integerBreak1(k + 1, n, count, p, ls)

    def integerBreak(self, n: int) -> int:
        ls = [1]

        self.integerBreak1(1, n, 0, 1, ls)

        return ls[0]