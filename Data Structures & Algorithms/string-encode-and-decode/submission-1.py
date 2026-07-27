class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes,res = [], ""
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz)
            res += ","
        res += "#"
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, out, i = [], [], 0
        while s[i] != "#":
            curr = ""
            while s[i] != ",":
                curr += str(s[i])
                i += 1
            if curr:
                # print(f"curr={curr}")
                sizes.append(int(curr))
            i += 1
        i = i + 1
        for sz in sizes:
            out.append(s[i:i+sz])
            i += sz
        return out
        
