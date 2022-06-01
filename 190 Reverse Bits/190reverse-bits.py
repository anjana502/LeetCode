class Solution:
    def binary(self, n):
        b = ""
        while (n != 0):
            r = n % 2
            b = b + str(r)
            n = n // 2
        if (len(b) < 32):
            d = 32 - len(b)
            s = '0' * d
            b = b + s
        return b
    
    def reverseBits(self, n: int) -> int:
        b = self.binary(n)
        print(b)
        m = 0
        p = 31
        i = 0
        while (i < 32):
            m += int(b[i]) * (2 ** p)
            i += 1
            p -= 1
        return m
        