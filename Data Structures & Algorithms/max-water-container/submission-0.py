class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ar = 0
        n = len(heights)
        for i, h in enumerate(heights):
            for j in range(i+1, n):
                curr = (j - i) * min(h, heights[j])
                if curr > ar:
                    ar = curr
        return ar
        