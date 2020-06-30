class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[0 for x in range(n)] for y in range(n)]
        res = ""

        i = 0
        while i < n:
            dp[i][i] = 1
            res = s[i]
            i += 1

        i = 0
        j = 1
        while j < n:
            if s[i] == s[j]:
                dp[i][j] = 1
                res = s[i:j+1]
            else:
                dp[i][j] = 0
            i += 1
            j += 1

        k = 2
        while k < n:
            i = 0
            j = k
            while j < n:
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = 1
                    res = s[i:j+1]
                else:
                    dp[i][j] = 0
                i += 1
                j += 1
            k += 1

        return res

s = Solution()
print(s.longestPalindrome("cbbd"))

