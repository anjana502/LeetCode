class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 0
        max1 = 0
        j = 0

        for i in range(len(nums)):
            if (nums[i] == 1):
                count += 1
            
            while (j < i and (i - j + 1) > (count + 1)):
                if (nums[j] == 1):
                    count -= 1
                j += 1
            
            max1 = max(max1, count)
        
        if (max1 == len(nums)):
            max1 -= 1
        return max1