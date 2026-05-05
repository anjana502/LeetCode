class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left = [1 for i in range(n)]
        right = [1 for i in range(n)]
        left[0] = 0

        for i in range(2, n):
            if (nums[i - 1] <= nums[i - 2]):
                left[i] = left[i - 1] + 1
        
        right[n - 1] = 0

        for i in range(n - 3, -1, -1):
            if (nums[i + 1] <= nums[i + 2]):
                right[i] = right[i + 1] + 1
        
        ls1 = []

        for i in range(k, n - k):
            if (left[i] >= k and right[i] >= k):
                ls1.append(i)
        
        return ls1