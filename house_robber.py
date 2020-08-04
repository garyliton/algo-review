def rob(nums):
    if not nums:
        return 0

    if len(nums) <= 2:
        return max(nums)

    a = nums[0]
    b = max(nums[1], a)

    for num in nums[2:]:
        c = max(a+num, b)
        a = b
        b = c

    return c

print(rob([5,1,1,5]))