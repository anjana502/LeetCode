class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = {}
        max1 = 0
        sum1 = 0

        for i in range(len(nums)):
            sum1 += nums[i]

            if (sum1 == k):
                max1 = max(max1, i + 1)
            if ((sum1 - k) in d):
                max1 = max(max1, i - d[sum1 - k])
            
            if (sum1 not in d):
                d[sum1] = i
        
        return max1