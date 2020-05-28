def single_number(nums):
    # hash table
    htable = {}

    for num in nums:
        if num not in htable:
            htable[num] = 1
        else:
            htable[num] += 1

    for x in htable:
        if htable[x] == 1:
            return x

    # bit manipulation
    a = 0
    for i in nums:
        a ^= i
    return a

single_number([4,2, 1, 2,1])