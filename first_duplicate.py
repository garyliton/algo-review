def firstDuplicate(a):
    hashset = set()

    for num in a:
        if num in hashset:
            return num
        else:
            hashset.add(num)

    return -1

