class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ls = [[1]]
        if (rowIndex == 0):
            return ls[0]
        for i in range(2, rowIndex + 2):
            prev = [0] + ls[-1] + [0]
            cur = []
            for j in range(len(prev) - 1):
                cur.append(prev[j] + prev[j + 1])
            ls.append(cur)
        return ls[-1]