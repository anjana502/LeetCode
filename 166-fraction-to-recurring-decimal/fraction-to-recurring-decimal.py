class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if (numerator == 0):
            return "0"
        
        ls = []
        flag1 = 1 if (numerator > 0) else -1
        flag2 = 1 if (denominator > 0) else -1
        numerator = abs(numerator)
        denominator = abs(denominator)

        if (flag1 * flag2 < 0):
            ls.append("-")
        
        q = numerator // denominator
        r = numerator % denominator
        ls.append(str(q))

        if (r == 0):
            s = "".join(ls)

            return s
        
        ls.append(".")
        p = len(ls)
        d = {}
        d[r] = p

        while (r != 0):
            n = r * 10
            q = n // denominator
            r1 = n % denominator
            ls.append(str(q))

            if (r1 in d):
                ls.insert(d[r1], "(")
                ls.append(")")
                break
            
            d[r1] = len(ls)
            r = r1
        
        s = "".join(ls)

        return s