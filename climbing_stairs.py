def climbStairs(n):
    if n <= 2:
        return n

    a = 1
    b = 2
    c = a + b
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c

    return c

