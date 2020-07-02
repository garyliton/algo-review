
class Solution:
    def numSquares(self, n):
        if n <= 3:
            return n

        dp = [i for i in range(n + 1)]
        for i in range(4, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]


s = Solution()
print(s.numSquares(13))
