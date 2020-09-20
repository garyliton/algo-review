def pancakeSort(A):
    unsorted_idx = len(A)
    res = []

    while unsorted_idx != 1:
        greatest_num_idx = find_greatest_idx(A[:unsorted_idx])
        if greatest_num_idx != 0:
            res.append(greatest_num_idx + 1)
        res.append(unsorted_idx)
        unsorted_idx -= 1

    return res


def find_greatest_idx(lst):
    greatest_num = float('-inf')
    greatest_idx = 0

    for i in range(len(lst)):
        if lst[i] > greatest_num:
            greatest_num = lst[i]
            greatest_idx = i

    return greatest_idx

print(pancakeSort((3,2,4,1)))
