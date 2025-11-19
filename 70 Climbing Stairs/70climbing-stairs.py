class Solution:
    def climbStairs(self, n: int) -> int:
        if (n == 1):
            return 1

        ls = [0 for i in range(n + 1)]
        ls[1] = 1
        ls[2] = 2

        for i in range(3, n + 1):
            ls[i] = ls[i - 1] + ls[i - 2]
        
        return ls[n]