class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0

        for i in logs:
            if (i == "../"):
                if (level > 0):
                    level -= 1
            elif (i == "x/"):
                level += 1
            elif (i == "./"):
                continue
            else:
                level += 1
        
        return level