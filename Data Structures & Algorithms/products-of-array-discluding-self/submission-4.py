class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # prefix, suffix = [1] * n,  [1] * n
        # for i in range(1, n):
        #     prefix[i] = prefix[i-1] * nums[i-1]
        # print(f"prefix={prefix}")
        # for j in range(n-2, -1, -1):
        #     suffix[j] = suffix[j+1] * nums[j+1]
        # print(f"suffix={suffix}")
        # out = []
        # for i in range(n):
        #     out.append(prefix[i] * suffix[i])
        # return out
        # out = [0] * n
        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if i==j:
        #             continue
        #         prod = prod * nums[j]
        #     out[i] = prod
        # return out
        zero_count, prod, n = 0, 1, len(nums)
        for num in nums:
            if num:
                prod = prod * num
            else:
                zero_count += 1
        if zero_count >= 2:
            return [0] * n
        out = [0] * n
        for i, num in enumerate(nums):
            if zero_count:
                out[i] = 0 if num else prod
            else:
                out[i] = prod//num
        return out


