def anagram_difference(s, t):
    if len(s) != len(t):
        return - 1

    hash_map = {}
    for char in s:
        if char in hash_map:
            hash_map[char] += 1
        else:
            hash_map[char] = 1

    for char in t:
        if char in hash_map:
            hash_map[char] -= 1
            if hash_map[char] == 0:
                hash_map.pop(char)

    return sum(hash_map.values())

anagram_difference("anagram", "mangaar")