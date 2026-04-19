class Solution:
    def maximumSwap(self, num: int) -> int:
        num = str(num)
        ans = num

        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                if (num[j] > num[i]):
                    ls = list(num)
                    ls[i], ls[j] = ls[j], ls[i]
                    s = "".join(ls)

                    if (s > ans):
                        ans = s
        
        ans = int(ans)
        
        return ans