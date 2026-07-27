class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_index = {}
        for idx, val in enumerate(nums):
            val_index[val] = idx

        for idx, val in enumerate(nums):
            diff = target - val
            if diff in val_index and val_index[diff] != idx:
                return [idx, val_index[diff]]

        
        