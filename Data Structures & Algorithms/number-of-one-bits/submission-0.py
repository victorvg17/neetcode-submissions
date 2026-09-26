class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_len = 32
        num_ones = 0
        for i in range(32):
            if (n & (1 << i) > 0):
                num_ones += 1 
        return num_ones

        