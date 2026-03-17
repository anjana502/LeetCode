class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        j = 0
        max1 = 0

        for i in range(len(nums)):
            if (nums[i] == 0):
                count += 1
            
            while (j <= i and count > k):
                if (nums[j] == 0):
                    count -= 1
                
                j += 1
            
            max1 = max(max1, (i - j + 1))
        
        return max1