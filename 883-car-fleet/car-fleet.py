class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ls = sorted(list(zip(position, speed)), key = lambda i: i[0])
        prev_time = 0
        count = 0

        for i in range(len(ls) - 1, -1, -1):
            curr_time = (target - ls[i][0]) / ls[i][1]

            if (curr_time > prev_time):
                count += 1
                prev_time = curr_time
        
        return count