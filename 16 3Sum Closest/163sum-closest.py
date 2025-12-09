class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sum2 = 0
        min1 = float("inf")

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while (j < k):
                sum1 = nums[i] + nums[j] + nums[k]
                d = abs(target - sum1)

                if (d < min1):
                    min1 = d
                    sum2 = sum1
                
                if (sum1 > target):
                    k -= 1
                else:
                    j += 1
        
        return sum2