class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == 0):
            return 0
        
        flag = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        n = divisor

        while (dividend >= divisor):
            d = n
            count = 1

            while (dividend >= d):
                dividend -= d
                quotient += count

                d *= 2
                count *= 2
        
        quotient *= flag

        if (quotient > 2 ** 31 - 1):
            return (2 ** 31 - 1)
        elif (quotient < -2 ** 31):
            return (-2 ** 31)
        
        return quotient