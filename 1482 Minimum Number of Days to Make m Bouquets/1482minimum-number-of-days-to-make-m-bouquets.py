class Solution:
    def canMakeBouquets(self, bloomDay, m, k, day):
        count = 0
        span_days = 0

        for i in range(len(bloomDay)):
            if (bloomDay[i] <= day):
                span_days += 1

                if (span_days == k):
                    count += 1
                    span_days = 0
            else:
                span_days = 0

        if (count >= m):
            return True
        return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low = 1
        high = max(bloomDay)
        result = -1

        while (low <= high):
            mid = low + (high - low) // 2

            if (self.canMakeBouquets(bloomDay, m, k, mid) == True):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result