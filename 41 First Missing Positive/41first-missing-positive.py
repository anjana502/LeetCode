class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        
        if (nums[0] > 0 and nums[0] != 1):
            return 1
        
        i = 1

        while (i < len(nums)):
            if (nums[i - 1] <= 0 and nums[i] > 0 and nums[i] != 1):
                return 1
            if (nums[i - 1] > 0 and nums[i] > 0 and abs(nums[i] - nums[i - 1]) > 1):
                return (nums[i - 1] + 1)
            i += 1
        
        if (nums[-1] <= 0):
            return 1
            
        return (nums[-1] + 1)