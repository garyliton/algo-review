class Solution:
    def findDisappearedNumbers(self, nums):
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]

        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                res.append(i + 1)

        return res

s = Solution()
s.findDisappearedNumbers([4,3,2,7,8,2,3,1])