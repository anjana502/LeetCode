class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if (numerator == 0):
            return "0"
        
        sign1 = 1 if (numerator > 0) else -1
        sign2 = 1 if (denominator > 0) else -1
        ls = []

        if (sign1 * sign2 == -1):
            ls.append("-")
        
        numerator = abs(numerator)
        denominator = abs(denominator)

        ls.append(str(numerator // denominator))
        r = numerator % denominator

        if (r == 0):
            s = "".join(ls)

            return s
        
        ls.append(".")
        d = {}

        while (r != 0):
            d[r] = len(ls)
            r *= 10
            ls.append(str(r // denominator))
            r1 = r % denominator

            if (r1 in d):
                ls.insert(d[r1], "(")
                ls.append(")")
                break
            
            r = r1
        
        s = "".join(ls)

        return s