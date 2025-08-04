class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        pivot_index = -1

        for i in range(len(nums) - 2, -1, -1):
            if (nums[i] < nums[i + 1]):
                pivot_index = i
                break
        
        if (pivot_index == -1):
            nums.reverse()
            return
        
        for i in range(len(nums) - 1, pivot_index, -1):
            if (nums[i] > nums[pivot_index]):
                nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
                break
        
        left = pivot_index + 1
        right = len(nums) - 1

        while (left < right):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        

        