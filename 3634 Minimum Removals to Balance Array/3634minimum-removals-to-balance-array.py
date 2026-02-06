class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        min1 = float("inf")

        for j in range(n):
            while ((i < n) and (nums[i] <= nums[j] * k)):
                i += 1
            
            min1 = min(min1, n - (i - j))
        
        return min1