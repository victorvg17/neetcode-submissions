class Solution:
    def reverseBitsLong(self, n: int) -> int:
        last_nums = []
        out = 0
        while n:
            last = n & 1
            last_nums.append(last)
            n = n >> 1
        
        start = 31
        for num in last_nums:
            out = (num << start) | out
            start -= 1
        return out
    
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            last = n & 1
            result = result << 1
            result = result | last
            n = n >> 1
        return result
        