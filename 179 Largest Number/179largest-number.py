from functools import cmp_to_key

class Solution:
    def largestNumber1(self, a, b):
        s1 = a + b
        s2 = b + a

        if (s1 > s2):
            return -1
        if (s1 < s2):
            return 1
        return 0
    
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        nums.sort(key = cmp_to_key(self.largestNumber1))
        s = "".join(nums)

        if (s.count("0") == len(s)):
            return "0"
        return s