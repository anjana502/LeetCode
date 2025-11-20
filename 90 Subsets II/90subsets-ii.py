class Solution:
    def subsetsWithDup1(self, i, nums, ls, ls1):
        if (i == len(nums)):
            ls.append(ls1[:])
            return
        
        ls1.append(nums[i])
        self.subsetsWithDup1(i + 1, nums, ls, ls1)
        ls1.pop()

        j = i + 1

        while (j < len(nums) and nums[j] == nums[i]):
            j += 1
        
        self.subsetsWithDup1(j, nums, ls, ls1)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ls = []
        ls1 = []

        self.subsetsWithDup1(0, nums, ls, ls1)

        return ls