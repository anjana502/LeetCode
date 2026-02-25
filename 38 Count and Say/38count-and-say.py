class Solution:
    def countAndSay(self, n: int) -> str:
        if (n == 1):
            return "1"
        
        prev = self.countAndSay(n - 1)
        curr = ""
        count = 1
        char = prev[0]

        for i in range(1, len(prev)):
            if (prev[i] == prev[i - 1]):
                count += 1
            else:
                curr = curr + str(count) + char
                count = 1
                char = prev[i]
        
        curr = curr + str(count) + char

        return curr