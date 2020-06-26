class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        found = set()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.twoSum(nums, i, res, found)

        return res

    def twoSum(selfself, nums, i, res, found):
        target = 0 - nums[i]
        low = i + 1
        high = len(nums) - 1

        while low < high:
            temp_sum = nums[low] + nums[high]
            if temp_sum < target:
                temp_low = nums[low]
                low += 1
                while temp_low == nums[low]:
                    low += 1
                    if low >= high:
                        break
            elif temp_sum > target:
                temp_high = nums[high]
                high -= 1
                while temp_high == nums[high]:
                    high -= 1
                    if high <= low:
                        break
            else:
                res.append([nums[i], nums[low], nums[high]])
                temp_low = nums[low]
                low += 1
                while temp_low == nums[low]:
                    low += 1
                    if low >= high:
                        break
                temp_high = nums[high]
                high -= 1
                while temp_high == nums[high]:
                    high -= 1
                    if high <= low:
                        break


s = Solution()
s.threeSum([0, 0, 0])



