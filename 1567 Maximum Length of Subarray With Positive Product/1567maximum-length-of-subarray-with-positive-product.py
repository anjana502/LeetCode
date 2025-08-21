class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max1 = 0
        i = 0
        start = 0
        p = 1

        while (i < len(nums)):
            if (nums[i] != 0):
                if (nums[i] > p * nums[i]):
                    p = nums[i]
                    start = i
                else:
                    p *= nums[i]

                if (p > 0):
                    max1 = max(max1, (i - start + 1))
            else:
                p = 1
                start = i + 1
            
            i += 1
        
        return max1