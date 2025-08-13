class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        i = 0
        flag = False

        while (i < len(s) and s[i] == " "):
            i += 1

        if (i < len(s) and (s[i] == "-" or s[i] == "+")):
            if (s[i] == "-"):
                flag = True
            i += 1
        
        while (i < len(s)):
            if (s[i].isdigit() == True):
                num = num * 10 + int(s[i])
                i += 1
            else:
                break
        
        if (flag == True):
            num *= -1

        if (num < -2 ** 31):
            num = -2 ** 31
        elif (num > 2 ** 31 - 1):
            num = 2 ** 31 - 1
        
        return num