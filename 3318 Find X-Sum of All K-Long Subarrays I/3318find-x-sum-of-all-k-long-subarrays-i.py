from collections import defaultdict

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        d = defaultdict(lambda: 0)
        ls = []

        for i in range(k):
            d[nums[i]] += 1
        
        for i in range(k, len(nums)):
            ls1 = [j * k for j, k in sorted(d.items(), key = lambda i: (-1 * i[1], -1 * i[0]))]

            sum1 = sum(ls1[:min(x, len(ls1))])

            ls.append(sum1)

            d[nums[i - k]] -= 1
            
            d[nums[i]] += 1
        
        ls1 = [j * k for j, k in sorted(d.items(), key = lambda i: (-1 * i[1], -1 * i[0]))]
        sum1 = sum(ls1[:min(x, len(ls1))])

        ls.append(sum1)

        return ls