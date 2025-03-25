class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]

        ls = []

        for i in range(len(nums) - 1):
            d = (nums[i] + nums[i + 1]) % 10
            ls.append(d)
        
        return self.triangularSum(ls)