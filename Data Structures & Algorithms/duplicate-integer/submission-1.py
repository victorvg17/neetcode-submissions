class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if (len(nums) == 0):
        #     return False;
        # nums = sorted(nums)
        # freq = {}
        # for num in nums:
        #     if num in freq:
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1
        # for (key, value) in freq.items():
        #     if value > 1:
        #         return True
        # return False
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        