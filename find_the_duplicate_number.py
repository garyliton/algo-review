class Solution:
    def findDuplicate(self, nums):
        p1 = nums[0]
        p2 = nums[0]

        while True:
            p1 = nums[p1]
            p2 = nums[nums[p2]]
            if p1 == p2:
                break

        p2 = p1
        p1 = nums[0]

        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]

        return p1

s = Solution()
print(s.findDuplicate([2,5,9,6,9,3,8,9,7,1]))