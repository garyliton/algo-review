class Solution:
    def isAlienSorted(self, words, order):
        if len(words) < 2:
            return True

        htable = {}
        count = 0
        for letter in order:
            htable[letter] = count
            count += 1

        def compare(word1, word2):
            i = j = 0
            while i < len(word1) and j < len(word2):
                if htable[word1[i]] < htable[word2[j]]:
                    return True
                elif htable[word1[i]] > htable[word2[j]]:
                    return False
                else:
                    i += 1
                    j += 1
            return len(word1) <= len(word2)

        for i in range(len(words) - 1):
            for j in range(1, len(words)):
                if not compare(words[i], words[j]):
                    return False

        return True


s = Solution()
s.isAlienSorted(["ubg","kwh"], "qcipyamwvdjtesbghlorufnkzx")