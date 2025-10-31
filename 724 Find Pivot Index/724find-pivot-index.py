class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = [0 for i in range(len(nums))]
        right = [0 for i in range(len(nums))]

        for i in range(1, len(left)):
            left[i] = left[i - 1] + nums[i - 1]
        
        for i in range(len(right) - 2, -1, -1):
            right[i] = right[i + 1] + nums[i + 1]
        
        for i in range(len(nums)):
            if (left[i] == right[i]):
                return i
        
        return -1