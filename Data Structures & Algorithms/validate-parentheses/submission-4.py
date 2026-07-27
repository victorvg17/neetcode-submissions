class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n==1:
            return False
        stack = []
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
        return True if not stack else False

        