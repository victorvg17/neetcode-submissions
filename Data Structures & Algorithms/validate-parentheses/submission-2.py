class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n==1:
            return False
        res = []
        open_br = ["(", "[", "{"]
        close_br = [")", "]", "}"]
        brac_mp = {key: value for key, value in zip(open_br, close_br)}
        for c in s:
            if c in open_br:
                res.append(c)
            else:
                if len(res) == 0:
                    return False 
                last = res.pop()
                brac_match = brac_mp[last]
                if brac_match != c:
                    return False
        if len(res) == 0:
            return True 
        return False

        