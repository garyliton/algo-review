def moveZeroes(nums):
    count = 0
    for num in nums:
        if num != 0:
            nums[count] = num
            count += 1

    while count < len(nums):
        nums[count] = 0
        count += 1
    return nums
