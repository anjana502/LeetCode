class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        s = set()
        sum1 = 0

        for i in range(len(nums)):
            j = i
            k = i + 1
            max1 = min1 = nums[i]

            while (j >= 0 and k < len(nums)):
                if ((j, k) not in s):
                    min1 = min(min1, nums[j], nums[k])
                    max1 = max(max1, nums[j], nums[k])
                    sum1 += (max1 - min1)
                    s.add((j, k))
                j -= 1
                k += 1
            
            j = i - 1
            k = i + 1
            max1 = min1 = nums[i]

            while (j >= 0 and k < len(nums)):
                if ((j, k) not in s):
                    min1 = min(min1, nums[j], nums[k])
                    max1 = max(max1, nums[j], nums[k])
                    sum1 += (max1 - min1)
                    s.add((j, k))
                
                j -= 1
                k += 1
        
        return sum1