class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum1 = float("-inf")
        curr_sum1 = float("-inf")

        for i in nums:
            curr_sum1 = max(curr_sum1 + i, i)
            sum1 = max(sum1, curr_sum1)
        
        return sum1