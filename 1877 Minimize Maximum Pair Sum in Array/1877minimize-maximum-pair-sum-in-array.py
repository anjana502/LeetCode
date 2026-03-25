class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = n // 2 - 1
        j = n // 2
        sum1 = 0
        max1 = 0

        while (i >= 0 and j < n):
            sum1 = nums[i] + nums[j]
            max1 = max(max1, sum1)
            i -= 1
            j += 1
        
        return max1