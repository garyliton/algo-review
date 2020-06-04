def rob(nums):
    if not nums:
        return 0

    if len(nums) <= 2:
        return max(nums)

    return max(helper(nums[:-1]), helper(nums[1:]))

def helper(nums):
    if len(nums) <= 2:
        return max(nums)

    a = nums[0]
    b = max(nums[0], nums[1])

    for num in nums[2:]:
        c = max(a + num, b)
        a = b
        b = c

    return c