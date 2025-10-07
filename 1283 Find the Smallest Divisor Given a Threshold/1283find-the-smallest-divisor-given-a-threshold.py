import math

class Solution:
    def canDivide(self, nums, threshold, divisor):
        sum1 = 0

        for i in nums:
            sum1 += ceil(i / divisor)
        
        print((divisor, sum1))

        if (sum1 <= threshold):
            return True
        return False

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        result = 0

        while (low <= high):
            mid = low + (high - low) // 2

            if (self.canDivide(nums, threshold, mid) == True):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result