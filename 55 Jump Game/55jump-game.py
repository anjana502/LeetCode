class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max1 = nums[0]

        for i in range(1, len(nums)):
            if (max1 < i):
                return False
            
            max1 = max(max1, nums[i] + i)
        
        return True