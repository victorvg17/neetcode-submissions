class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # val_index = {} # val -> index
        # for i, val in enumerate(nums):
        #     val_index[val] = i
        
        # for i, val in enumerate(nums):
        #     diff = target - val
        #     if diff in val_index and val_index[diff] != i:
        #         return [i, val_index[diff]]
        # return []
        

        # for val in sorted(nums):
        #     curr_sum = nums[s] + nums[e]
        #     if curr_sum == target:
        #         return [s, e]
        #     elif curr_sum < target:
        #         s += 1
        #     else:
        #         e -= 1

        val_idx = {} # val -> index
        for i, val in enumerate(nums):
            val_idx[val] = i

        for i, val in enumerate(nums):
            diff = target - nums[i]
            if diff in val_idx and val_idx[diff] != i:
                return [i, val_idx[diff]]
        return []

        
        