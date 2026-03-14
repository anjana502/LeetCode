class Solution:
    def rob(self, nums: List[int]) -> int:
        ls = [0 for i in range(len(nums) + 1)]
        ls[1] = nums[0]

        for i in range(2, len(nums) + 1):
            ls[i] = max(ls[i - 2] + nums[i - 1], ls[i - 1])
        
        return ls[-1]