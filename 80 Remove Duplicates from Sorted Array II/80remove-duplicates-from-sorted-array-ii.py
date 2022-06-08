class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if (i <= len(nums) - 3 and nums[i] == nums[i + 1] and nums[i] == nums[i + 2]):
                continue
            nums[j] = nums[i]
            j += 1
        return j