class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s_alpha = [i.lower() for i in s if i.isalnum()]
        # alpha_str = "".join(s_alpha)
        # print(f"alpha_str={alpha_str}")
        # i, j = 0, len(alpha_str) - 1
        # while i <= j:
        #     if alpha_str[i] != alpha_str[j]:
        #         return False
        #     if i==j:
        #         break
        #     i += 1
        #     j -= 1
        # return True
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
        