class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = set()
        ls = []

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while (j < k):
                sum1 = nums[i] + nums[j] + nums[k]

                if (sum1 == 0):
                    s.add((nums[i], nums[j], nums[k]))
                if (sum1 <= 0):
                    j += 1
                else:
                    k -= 1
        
        for i in s:
            ls.append(list(i))
        
        return ls