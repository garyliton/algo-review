class Solution:
    def firstMissingPositive(self, nums):
        has_one = False
        for i in range(len(nums)):
            if nums[i] == 1:
                has_one = True
            elif nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1

        if not has_one:
            return 1

        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] = -nums[abs(num) - 1]

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        return len(nums) + 1
