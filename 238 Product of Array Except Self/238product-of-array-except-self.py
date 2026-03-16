class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for i in range(len(nums))]
        right = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        
        for j in range(len(nums) - 2, -1, -1):
            right[j] = right[j + 1] * nums[j + 1]
        
        ls = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            ls[i] = left[i] * right[i]
        
        return ls