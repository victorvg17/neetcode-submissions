class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = {}
        for num in nums:
            out[num] = out.get(num, 0) + 1
        # out = {k: v for k,v in sorted(out.items(), key = lambda x: x[1], reverse=True)}
        # return list(out.keys())[:k]
        arr = []
        for num, cnt in out.items():
            arr.append([cnt, num])
        arr = sorted(arr)
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        