class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        prev = 0

        for i in range(len(nums)):
            if (nums[i] != val):
                nums[prev] = nums[i]
                prev += 1
        
        return prev