from collections import defaultdict

class Solution:
    def countSubarrays(self, nums, k):
        d = defaultdict(lambda: 0)
        j = 0
        count = 0

        for i in range(len(nums)):
            d[nums[i]] += 1

            while (j <= i and len(d) > k):
                d[nums[j]] -= 1

                if (d[nums[j]] == 0):
                    del d[nums[j]]
                
                j += 1
            
            count += (i - j + 1)
        
        return count
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count1 = self.countSubarrays(nums, k)
        count2 = self.countSubarrays(nums, k - 1)

        count = count1 - count2

        return count