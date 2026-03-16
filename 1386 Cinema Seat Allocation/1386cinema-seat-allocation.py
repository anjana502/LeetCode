from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        d = defaultdict(set)

        for row, col in reservedSeats:
            d[row].add(col)

        count = 2 * (n - len(d))

        for row in d:
            group_1 = all(i not in d[row] for i in [2, 3, 4, 5])
            group_2 = all(i not in d[row] for i in [4, 5, 6, 7])
            group_3 = all(i not in d[row] for i in [6, 7, 8, 9])

            if (group_1 == True):
                count += 1
            if (group_3 == True):
                count += 1
            if (group_2 == True and group_1 == False and group_3 == False):
                count += 1
                
        return count