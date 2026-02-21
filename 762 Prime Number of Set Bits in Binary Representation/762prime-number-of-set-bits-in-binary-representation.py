from math import ceil, log2

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ls = [0 for i in range(ceil(log2(right)) + 1)]
        flag = [True for i in range(ceil(log2(right)) + 1)]
        flag[0] = False
        flag[1] = False

        for i in range(left, right + 1):
            count = 0
            j = i

            while (j != 0):
                j = j & (j - 1)
                count += 1

            ls[count] += 1

        for i in range(2, len(flag)):
            j = i * i

            while (j < len(flag)):
                flag[j] = False
                j += i

        result = 0

        for i in range(len(ls)):
            if (flag[i] == True):
                result += ls[i]
        
        return result