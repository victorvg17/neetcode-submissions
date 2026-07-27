class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sort = "".join(sorted(s1))
        n2 = len(s2)
        n1 = len(s1)
        for i in range(n2):
            for j in range(n2):
                s2_sub = s2[i:j+1]
                s2_sub = "".join(sorted(s2_sub))
                if s2_sub == s1_sort:
                    return True
        return False
        