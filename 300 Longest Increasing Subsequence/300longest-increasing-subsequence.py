class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ls = []
        ls.append(nums[0])

        for i in range(1, len(nums)):
            if (nums[i] > ls[-1]):
                ls.append(nums[i])
            else:
                low = 0
                high = len(ls) - 1

                while (low < high):
                    mid = low + (high - low) // 2

                    if (nums[i] > ls[mid]):
                        low = mid + 1
                    else:
                        high = mid
                
                ls[low] = nums[i]
        
        return len(ls)