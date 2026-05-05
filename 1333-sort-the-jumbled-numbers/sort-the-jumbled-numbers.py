class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mappingDigits(n):
            n = str(n)
            s1 = ""

            for i in n:
                s1 += str(mapping[int(i)])
            
            s1 = int(s1)
            
            return s1

        nums.sort(key = mappingDigits)

        return nums