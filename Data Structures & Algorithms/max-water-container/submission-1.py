class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # ar = 0
        # n = len(heights)
        # for i, h in enumerate(heights):
        #     for j in range(i+1, n):
        #         curr = (j - i) * min(h, heights[j])
        #         if curr > ar:
        #             ar = curr
        # return ar
        ar = 0
        n = len(heights)
        l, r = 0, n-1
        while l<r:
            curr = (r - l) * min(heights[l], heights[r])
            if curr > ar:
                ar = curr
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return ar


        