from collections import defaultdict

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d = defaultdict(lambda: 0)
        sum1 = 0
        j = 0
        max1 = -1

        for i in range(len(nums)):
            d[nums[i]] += 1
            sum1 += nums[i]

            while ((j < i) and (d[nums[i]] > 1)):
                d[nums[j]] -= 1
                sum1 -= nums[j]
                j += 1
            
            max1 = max(max1, sum1)
        
        return max1