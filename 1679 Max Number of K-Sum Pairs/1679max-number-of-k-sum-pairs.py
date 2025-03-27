class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        count = 0

        while (i < j):
            sum1 = nums[i] + nums[j]
            if (sum1 == k):
                nums[i] = float('inf')
                nums[j] = float('inf')
                count += 1
            if (sum1 <= k):
                i += 1
            else:
                j -= 1
        
        return count