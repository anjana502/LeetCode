class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = 0
        max1 = 0
        sum1 = 0

        for i in range(len(nums)):
            sum1 += nums[i]

            while (nums[i] * (i - j + 1) - sum1 > k):
                sum1 -= nums[j]
                j += 1
            
            max1 = max(max1, (i - j + 1))
        
        return max1