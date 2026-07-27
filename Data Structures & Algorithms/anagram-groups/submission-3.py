class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # keys = set()
        # for s in strs:
        #     s_sorted = "".join(sorted(s))
        #     keys.add(s_sorted)
        
        # out = {k: [] for k in keys}
        out = {}
        for s in strs:
            s_sort = "".join(sorted(s))
            if s_sort not in out:
                out[s_sort] = []
            out[s_sort].append(s)
        return [out[k] for k in out]



        