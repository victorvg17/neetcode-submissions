class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = set()
        for s in strs:
            s_sorted = "".join(sorted(s))
            keys.add(s_sorted)
        
        out = {k: [] for k in keys}
        for s in strs:
            s_sorted = "".join(sorted(s))
            out[s_sorted].append(s)
            # if s_sorted in keys:
                
        return [out[k] for k in out]



        