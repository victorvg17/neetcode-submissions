class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {k: v for k,v in sorted(count.items(), key = lambda x: x[1], reverse=True)}
        # return list(count.keys())[:k]
        # arr = []
        # for num, cnt in count.items():
        #     arr.append([cnt, num])
        # arr = sorted(arr)
        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        # return res
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        freq = [[] for i in range(0, len(nums)+1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
        # freq = sorted(freq)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res