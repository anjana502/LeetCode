class Solution:
    def checkValidString(self, s: str) -> bool:
        count = 0
        count1 = 0

        for i in s:
            if (i =="("):
                count += 1
            elif (i == "*"):
                count1 += 1
            else:
                if (count > 0):
                    count -= 1
                elif (count1 > 0):
                    count1 -= 1
                else:
                    return False
        
        count = 0
        count1 = 0

        for i in s[::-1]:
            if (i == ")"):
                count += 1
            elif (i == "*"):
                count1 += 1
            else:
                if (count > 0):
                    count -= 1
                elif (count1 > 0):
                    count1 -= 1
                else:
                    return False
        
        return True