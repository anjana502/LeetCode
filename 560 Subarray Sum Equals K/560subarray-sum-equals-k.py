from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(lambda: 0)
        sum1 = 0
        count = 0

        for i in nums:
            sum1 += i

            if (sum1 == k):
                count += 1
            if ((sum1 - k) in d):
                count += d[sum1 - k]
            
            d[sum1] += 1
        
        return count