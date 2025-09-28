class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d = {i: "" for i in range(numRows)}
        row = 0
        flag = True

        for i in s:
            d[row] += i

            if (row == (numRows) - 1):
                flag = False
            elif (row == 0):
                flag = True

            if (flag == True):
                row += 1
            else:
                row -= 1 if (row > 0) else 0
        
        s1 = ""
        num = 0

        while (num in d):
            s1 += d[num]
            num += 1
        
        return s1