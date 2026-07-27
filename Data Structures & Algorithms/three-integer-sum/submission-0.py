class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 3 and nums == [0, 0, 0]:
            return [nums]
        nums = sorted(nums)
        out = []
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if (nums[i] + nums[j] + nums[k] == 0):
                        new = [nums[i], nums[j], nums[k]]
                        if new not in out:
                            out.append([nums[i], nums[j], nums[k]])
        return out

        