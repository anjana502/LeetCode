class Solution:
    def jump(self, nums: List[int]) -> int:
        max1 = float("-inf")
        index = 0
        count = 0

        for i in range(len(nums) - 1):
            max1 = max(max1, nums[i] + i)

            if (i == index):
                count += 1
                index = max1
        
        return count