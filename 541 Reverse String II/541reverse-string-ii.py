class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        ls = list(s)

        while (i < len(ls)):
            l = i
            h = min(len(s) - 1, i + k - 1)

            while (l < h):
                ls[l], ls[h] = ls[h], ls[l]
                l += 1
                h -= 1
            
            i += 2 * k
        
        s = "".join(ls)

        return s