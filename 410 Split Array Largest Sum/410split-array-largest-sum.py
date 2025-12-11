class Solution:
    def canSplit(self, nums, k, mid):
        count = 1
        sum1 = 0

        for i in nums:
            if (sum1 + i > mid):
                count += 1
                sum1 = i
            else:
                sum1 += i
        
        if (count <= k):
            return True
        return False
    
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        result = -1

        while (low <= high):
            mid = low + (high - low) // 2

            if (self.canSplit(nums, k, mid) == True):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result