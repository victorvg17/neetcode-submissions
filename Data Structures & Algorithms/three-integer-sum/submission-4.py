class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # out = set()
        # out = []
        # nums = sorted(nums)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1,n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 tmp = [nums[i],nums[j],nums[k]]
        #                 out.add(tuple(tmp))
        # return [list(i) for i in out]
        out = []
        nums = sorted(nums)
        n = len(nums)
        # if nums[0] > 0:
        #     return []
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i>0 and a == nums[i-1]:
                continue
            targ = -nums[i]
            l, r = i + 1, n - 1
            while l < r:
                if nums[l] + nums[r] > targ:
                    r -= 1
                elif nums[l] + nums[r] < targ:
                    l += 1
                else:
                    out.append([a, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1 

        return out



        