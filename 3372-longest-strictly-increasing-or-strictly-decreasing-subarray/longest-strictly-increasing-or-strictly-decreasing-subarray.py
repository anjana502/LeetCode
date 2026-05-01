class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max1 = -1
        d = 1

        for i in range(1, len(nums)):
            if (nums[i] > nums[i - 1]):
                d += 1
            else:
                max1 = max(max1, d)
                d = 1
        
        max1 = max(max1, d)

        d = 1

        for i in range(1, len(nums)):
            if (nums[i] < nums[i - 1]):
                d += 1
            else:
                max1 = max(max1, d)
                d = 1
        
        max1 = max(max1, d)
        
        return max1