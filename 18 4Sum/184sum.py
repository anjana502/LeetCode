class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ls = []
        s = set()

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                k = j + 1
                l = len(nums) - 1

                while (k < l):
                    sum1 = nums[i] + nums[j] + nums[k] + nums[l]

                    if (sum1 == target):
                        ls1 = sorted([nums[i], nums[j], nums[k], nums[l]])
                        s.add(tuple(ls1))
                        k += 1
                    elif (sum1 < target):
                        k += 1
                    else:
                        l -= 1
        
        for i in s:
            ls.append(list(i))

        return ls