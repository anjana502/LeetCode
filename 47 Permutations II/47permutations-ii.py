class Solution:
    def permutations1(self, nums, l, h, s):
        if (l == h):
            s.add(tuple(nums[:]))
            return
        
        for i in range(l, h + 1):
            nums[l], nums[i] = nums[i], nums[l]
            self.permutations1(nums, l + 1, h, s)
            nums[l], nums[i] = nums[i], nums[l]
            
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ls = []
        s = set()

        self.permutations1(nums, 0, len(nums) - 1, s)

        for i in s:
            ls.append(list(i))

        return ls