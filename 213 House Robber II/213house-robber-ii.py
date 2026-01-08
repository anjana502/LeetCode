class Solution:
    def rob1(self, nums):
        ls = [0 for i in range(len(nums) + 1)]
        ls[1] = nums[0]

        for i in range(2, len(nums) + 1):
            ls[i] = max(nums[i-1] + ls[i-2], ls[i-1])
        
        return ls[-1]
    
    def rob(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]
        
        d1 = self.rob1(nums[1:])
        d2 = self.rob1(nums[:-1])
        
        max1 = max(d1, d2)

        return max1