class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if prices == sorted(prices, reverse=True):
            return 0
        pr = 0
        for i, p in enumerate(prices):
            for j in range(i+1, n):
                if p < prices[j]:
                    pr = max(pr, prices[j] - p)
        return pr