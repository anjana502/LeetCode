class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        ls = []

        def mappingDigits(n):
            n = str(n)
            s1 = ""

            for i in n:
                s1 += str(mapping[int(i)])
            
            s1 = int(s1)
            
            return s1

        for i in range(len(nums)):
            s = mappingDigits(nums[i])
            ls.append((nums[i], s, i))

        ls.sort(key = lambda i: (i[1], i[2]))
        ls = [ls[i][0] for i in range(len(ls))]

        return ls