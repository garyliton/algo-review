class Solution:
    def isAnagram(self, s, t):
        hashtable = {}

        for char in s:
            if char not in hashtable:
                hashtable[char] = 1
            else:
                hashtable[char] += 1

        for char in t:
            if char not in hashtable:
                return False
            else:
                hashtable[char] -= 1
                if hashtable[char] == 0:
                    hashtable.pop(char)

        return len(hashtable) == 0


