class Solution:
    def numDecodings(self, s: str):
        if len(s) == 0:
            return 0

        dp = [0 for x in range(len(s) + 1)]

        dp[0] = 1
        dp[1] = 1 if int(s[0]) >= 1 else 0

        for i in range(2, len(s) + 1):
            cur_digit = int(s[i-1])
            last_two_digits = int(s[i-2:i])

            if cur_digit >= 1:
                dp[i] += dp[i-1]

            if last_two_digits >= 10 and last_two_digits <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]





