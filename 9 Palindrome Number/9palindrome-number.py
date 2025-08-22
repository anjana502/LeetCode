class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        
        n = x
        m = 0

        while (x > 0):
            r = x % 10
            m = m * 10 + r
            x = x // 10
        
        if (n == m):
            return True
        return False