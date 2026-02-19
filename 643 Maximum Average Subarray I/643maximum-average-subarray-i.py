class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum1 = 0
        max1 = float("-inf")

        for i in range(len(nums)):
            sum1 += nums[i]

            if (i >= k):
                sum1 -= nums[i - k]
            
            if (i >= (k - 1)):
                max1 = max(max1, sum1)
        
        avg = max1 / k

        return avg