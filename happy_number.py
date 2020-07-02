def happyNumber(n):
    hashset = set()
    cur_sum = get_sum(n)
    hashset.add(cur_sum)

    while cur_sum != 1:
        cur_sum = get_sum(cur_sum)
        if cur_sum in hashset:
            return False
        else:
            hashset.add(cur_sum)

    return True


def get_sum(n):
    sum = 0
    num_str = str(n)

    for char in num_str:
        sum += int(float(char)) * int(float(char))

    return sum

def get_next(n):
    total_sum = 0
    while n > 0:
        n, digit = divmod(n, 10)
        print(digit)

print(get_next(123))

