def maxSubArray(nums):
    msf = nums[0]
    mf = nums[0]

    for num in nums[1:]:
        msf = max(num, msf + num)
        if msf > mf:
            mf = msf

    return mf