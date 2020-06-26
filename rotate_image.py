def rotateImage(a):
    for row in range(len(a)):
        for col in range(row, len(a)):
            a[col][row], a[row][col] = a[row][col], a[col][row]

    for i in range(len(a)):
        a[i].reverse()

    return a
