class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for i in logs:
            ls1 = i.split(" ")
            if (ls1[1].isdigit() == True):
                digit_logs.append(i)
            else:
                letter_logs.append((ls1[0], ls1[1:]))
        
        letter_logs.sort(key = lambda i: (i[1], i[0]))

        ls = []

        for i in letter_logs:
            s = i[0] + " " + " ".join(i[1])
            ls.append(s)
        
        ls.extend(digit_logs)

        return ls