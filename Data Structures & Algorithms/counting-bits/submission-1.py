class Solution:
    def hammingCode(self, num: int) -> num:
        out = 0
        while num:
            if (num) & 1:
                out += 1
            num = num >> 1
        return out
    def countBitsHc(self, n: int) -> List[int]:
        out = []
        for i in range(0, n+1):
            out.append(self.hammingCode(i))
        return out
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        for i in range(0, n+1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp