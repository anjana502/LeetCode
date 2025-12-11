class Solution:
    def validateIPv4(self, queryIP):
        ls = queryIP.split(".")

        if (len(ls) != 4):
            return "Neither"
        
        for i in ls:
            if ((len(i) == 0) or (i[0] == "0" and len(i) > 1) or (i.isdigit() == False) or (int(i) < 0) or (int(i) > 255)):
                return "Neither"
        
        return "IPv4"
    
    def isHexadecimalValue(self, s):
        try:
            d = int(s, 16)
            return True
        except ValueError:
            return False
        
    def validateIPv6(self, queryIP):
        ls = queryIP.split(":")

        if (len(ls) != 8):
            return "Neither"
        
        for i in ls:
            if ((len(i) < 1) or (len(i) > 4) or (self.isHexadecimalValue(i) == False)):
                return "Neither"
        
        return "IPv6"
    
    def validIPAddress(self, queryIP: str) -> str:
        if ("." in queryIP):
            return self.validateIPv4(queryIP)
        elif (":" in queryIP):
            return self.validateIPv6(queryIP)
        return "Neither"