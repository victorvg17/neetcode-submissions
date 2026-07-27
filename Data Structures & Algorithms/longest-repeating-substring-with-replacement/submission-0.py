class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        lmax = 0
        for i in range(n):
            for j in range(i, n):
                mp = {}
                n_sb = j-i+1
                s_sb = s[i:j+1]
                fmax = 0
                for c in s_sb:
                    mp[c] = mp.get(c, 0) + 1
                    fmax = max(mp[c], fmax)
                
                n_rep = n_sb - fmax
                if n_rep <= k and n_sb > lmax:
                    lmax = n_sb
        return lmax

        