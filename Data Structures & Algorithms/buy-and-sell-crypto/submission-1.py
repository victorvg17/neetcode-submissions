class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if prices == sorted(prices, reverse=True) or n == 1:
            return 0
        
        # for i, p in enumerate(prices):
        #     for j in range(i+1, n):
        #         if p < prices[j]:
        #             pr = max(pr, prices[j] - p)
        pr = 0
        b, s = 0, 1
        while s < n:
            if prices[b] <= prices[s]:
                pr = max(pr, prices[s] - prices[b])
            else:
                b = s
            s += 1
        return pr