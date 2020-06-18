class Solution:
    def subarraySum(self, nums, k):
        if len(nums) == 0:
            return 0

        sums = {}
        count = 0
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum == k:
                count += 1
            if (curr_sum - k) in sums:
                count += sums[curr_sum - k]
            if curr_sum in sums:
                sums[curr_sum] += 1
            else:
                sums[curr_sum] = 1
        return count

s = Solution()
print(s.subarraySum([0,0,0,0,0,0,0,0,0,0], 0))



