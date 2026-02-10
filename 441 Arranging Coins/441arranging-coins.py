class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 1
        high = n
        result = -1

        while (low <= high):
            mid = low + (high - low) // 2
            d = mid * (mid + 1) // 2

            if (d <= n):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return result