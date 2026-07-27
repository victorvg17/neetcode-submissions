class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        if len(set(s)) == 1:
            return 1
        lmax = 0
        for i in range(n):
            hs = set()
            hs.add(s[i])
            # lcurr = 1
            for j in range(i+1, n):
                if s[j] not in hs:
                    hs.add(s[j])
                    # lcurr += 1
                else:
                    break
            if len(hs) > lmax:
                lmax = len(hs)
        return lmax

        
        