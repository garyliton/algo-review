class Solution:
    def findDuplicates(self, nums):
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(num)
            else:
                nums[abs(num) - 1] = -nums[abs(num) - 1]

        return res

