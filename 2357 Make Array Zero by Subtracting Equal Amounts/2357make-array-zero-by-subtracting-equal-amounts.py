class Solution:
    def minimumOperations1(self, i, nums, ls):
        if (i == len(nums)):
            return
        if (nums[i] == 0):
            while (i < len(nums) and nums[i] == 0):
                i += 1
            
            return self.minimumOperations1(i, nums, ls)

        ls[0] += 1
        d = nums[i]

        for j in range(i, len(nums)):
            nums[j] -= d
        
        self.minimumOperations1(i + 1, nums, ls)
    
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        ls = [0]

        self.minimumOperations1(0, nums, ls)

        return ls[0]