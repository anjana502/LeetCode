class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        max1 = 0
        count = 0

        for i in range(len(s)):
            if (s[i] in vowels):
                count += 1
            
            if (i >= k):
                if (s[i - k] in vowels):
                    count -= 1
            
            max1 = max(max1, count)

        return max1 