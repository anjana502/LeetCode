from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sum1 = 0
        max1 = 0
        d = defaultdict(lambda: 0)
        j = 0

        for i in range(len(nums)):
            d[nums[i]] += 1
            sum1 += nums[i]
            
            while ((j < i) and ((d[nums[i]] > 1) or ((i - j + 1) > k))):
                d[nums[j]] -= 1
                sum1 -= nums[j]
                j += 1
            
            if ((d[nums[i]] == 1) and ((i - j + 1) == k)):
                max1 = max(max1, sum1)
        
        return max1