class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_index = {} # val -> index
        for i, val in enumerate(nums):
            val_index[val] = i
        
        for i, val in enumerate(nums):
            diff = target - val
            if diff in val_index and val_index[diff] != i:
                return [i, val_index[diff]]
        return []

        
        