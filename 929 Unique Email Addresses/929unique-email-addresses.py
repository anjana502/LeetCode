class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        
        for i in emails:
            ls = i.split("@")
            local_name = ""
            
            j = 0
            
            while (j < len(ls[0]) and ls[0][j] != "+"):
                if (ls[0][j] == "."):
                    j += 1
                    continue
                
                local_name += ls[0][j]
                j += 1
            
            s1 = local_name + "@" + ls[1]
            
            s.add(s1)
        
        d = len(s)
        
        return d