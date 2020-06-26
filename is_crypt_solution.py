def isCryptSolution(crypt, solution):
    hashmap = {}
    for row in solution:
        hashmap[row[0]] = int(row[1])

    res = [0, 0, 0]

    for i in range(len(crypt)):
        exp = 0
        word = crypt[i]
        for j in range(len(word) - 1, -1, -1):
            res[i] += hashmap[word[j]] * (10 ** exp)
            exp += 1

    return res[0] + res[1] == res[2]

isCryptSolution(["TEN", "TWO", "ONE"], [["O","1"],
 ["T","0"],
 ["W","9"],
 ["E","5"],
 ["N","4"]])