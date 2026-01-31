class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        ls = sorted(nums)
        low = 0
        high = len(ls) - 1
        mid = low + (high - low) // 2

        for i in range(len(nums)):
            if (i % 2 == 0):
                nums[i] = ls[mid]
                mid -= 1
            else:
                nums[i] = ls[high]
                high -= 1