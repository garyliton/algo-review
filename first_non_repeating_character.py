def firstNotRepeatingCharacter(s):
    hash_map = {}
    for char in s:
        if char in hash_map:
            hash_map[char] += 1
        else:
            hash_map[char] = 1

    for char in s:
        if hash_map[char] == 1:
            return char

    return "_"