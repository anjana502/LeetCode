from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(lambda: 0)
        j = 0

        for i in range(len(nums)):
            d[nums[i]] += 1

            while (d[nums[i]] > 1):
                if (nums[j] == nums[i] and (i - j) <= k):
                    return True
                
                d[nums[j]] -= 1
                j += 1
        
        return False