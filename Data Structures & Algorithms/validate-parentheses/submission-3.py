class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n==1:
            return False
        stack = []
        # open_br = ["(", "[", "{"]
        # close_br = [")", "]", "}"]
        # brac_mp = {key: value for key, value in zip(open_br, close_br)}
        brace_map = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c in brace_map:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False 
                last = stack.pop()
                brac_match = brace_map[last]
                if brac_match != c:
                    return False
        if len(stack) == 0:
            return True 
        return False

        