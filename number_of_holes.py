def count_holes(num):
    holes = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1]
    count = 0

    while num > 0:
        num, digit = divmod(num, 10)
        count += holes[digit]

    return count

print(count_holes(6457819))