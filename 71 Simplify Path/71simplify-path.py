class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0

        while (i < len(path)):
            if (path[i] == "."):
                s = ""

                while (i < len(path) and path[i] != "/"):
                    s += path[i]
                    i += 1
                
                if (s == ".." and len(stack) != 0):
                    stack.pop()
                elif (s != ".." and len(s) >= 2):
                    stack.append(s)
            elif (path[i] == "/"):
                while (i < len(path) and path[i] == "/"):
                    i += 1
            else:
                s = ""

                while (i < len(path) and path[i] != "/"):
                    s += path[i]
                    i += 1
                
                stack.append(s)
        
        s1 = "/" + "/".join(stack)
        
        return s1