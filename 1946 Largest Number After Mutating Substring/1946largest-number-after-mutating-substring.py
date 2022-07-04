class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        flag = False
        for i in range(len(num)):
            if (change[int(num[i])] > int(num[i])):
                flag = True
                num = num[:i] + str(change[int(num[i])]) + num[i + 1:]
            elif (change[int(num[i])] == int(num[i])):
                pass
            else:
                if (flag == True):
                    return num
        return num
            