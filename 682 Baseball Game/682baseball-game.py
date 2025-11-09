class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []

        for i in operations:
            if (i == "+"):
                sum1 = s[-1] + s[-2]
                s.append(sum1)
            elif (i == "D"):
                d = 2 * s[-1]
                s.append(d)
            elif (i == "C"):
                s.pop()
            else:
                s.append(int(i))
        
        sum1 = 0

        for i in s:
            sum1 += i
        
        return sum1