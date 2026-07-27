class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        if len(strs) == 1:
            return [[strs[0]]]
        keys = set()
        for s in strs:
            s_sorted = "".join(sorted(s))
            keys.add(s_sorted)
        
        out = {k: [] for k in keys}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in keys:
                out[s_sorted].append(s)
        print(f"out={out}")
        return [out[k] for k in out]



        