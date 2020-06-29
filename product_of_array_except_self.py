class Solution:
    def productExceptSelf(self, nums):
        res = [nums[0]]
        product = 1

        for i in range(1, len(nums)):
            res.append(nums[i] * res[i-1])

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                res[-1] = res[-2]
                product = product * nums[i]
            elif i == 0:
                res[i] = product
            else:
                res[i] = res[i-1] * product
                product = product * nums[i]

        return res

s = Solution()
s.productExceptSelf([2,3,5,0])

