class Solution:
    def missingNumber(self, nums):
        total_sum = sum(list(range(0, len(nums) + 1)))

        nums_sum = sum(nums)

        if total_sum == nums_sum:
            return 0

        return total_sum - nums_sum