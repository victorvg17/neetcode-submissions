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

        # 2 pointer approach
        A = [] # list of [val, idx]
        for i, num in enumerate(nums):
            A.append([num, i])
        A.sort()
        i,j = 0, len(A) - 1

        while i<j:
            curr_sum = A[i][0] + A[j][0]
            if curr_sum == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif curr_sum < target:
                i += 1
            else:
                j -= 1
        return []
        


        
        