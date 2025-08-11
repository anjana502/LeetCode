class Solution:
    def minSwaps(self, s: str) -> int:
        count_0 = count_1 = 0

        for i in s:
            if (i == "0"):
                count_0 += 1
            else:
                count_1 += 1
        
        if (abs(count_0 - count_1) > 1):
            return -1
        
        s0s0 = s0s1 = s1s0 = s1s1 = 0

        for i in range(len(s)):
            if (i % 2 == 0 and s[i] != "0"):
                s0s0 += 1
            elif (i % 2 != 0 and s[i] != "1"):
                s0s1 += 1
        
        for i in range(len(s)):
            if (i % 2 == 0 and s[i] != "1"):
                s1s1 += 1
            elif (i % 2 != 0 and s[i] != "0"):
                s1s0 += 1

        min1 = 0
        if (s0s0 == s0s1 and s1s0 == s1s1):
            min1 = min(s0s0, s1s0)
        elif (s0s0 == s0s1):
            min1 = s0s0
        elif (s1s0 == s1s1):
            min1 = s1s0
        else:
            min1 = -1
        
        return min1