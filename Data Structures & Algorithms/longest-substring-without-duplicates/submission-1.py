class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        # if len(set(s)) == 1:
        #     return 1
        lmax, l = 0, 0
        hs = set()
        for r in range(n):
            while s[r] in hs:
                hs.remove(s[l])
                l += 1
            hs.add(s[r])
            lmax = max(lmax, r-l+1)
        return lmax
        # for i in range(n):
        #     hs = set()
        #     hs.add(s[i])
        #     for j in range(i+1, n):
        #         if s[j] not in hs:
        #             hs.add(s[j])
        #         else:
        #             break
        #     if len(hs) > lmax:
        #         lmax = len(hs)
        # return lmax

        
        