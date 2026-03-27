class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        max_index = -1
        max1 = -1
        n = len(nums)

        for i in range(n):
            if (nums[i] >= max1):
                max1 = nums[i]
                max_index = i
        
        count = (n - 1 - max_index)
        min_index = -1
        min1 = float("inf")

        for j in range(n - 1, -1, -1):
            if (nums[j] <= min1):
                min1 = nums[j]
                min_index = j if (j < max_index) else (j - 1)
        
        if (min_index != -1):
            count += min_index

        return count