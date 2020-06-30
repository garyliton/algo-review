class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        n = len(s)
        if n < 3:
            return n

        max_len = 2
        hash_table = {}
        left = right = 0

        while right < n:
            if len(hash_table) < 3:
                hash_table[s[right]] = right
                right += 1

            if len(hash_table) == 3:
                min_idx = min(hash_table.values())
                hash_table.pop(s[min_idx])
                left = min_idx + 1

            max_len = max(max_len, right - left)

        return max_len


s = Solution()
s.lengthOfLongestSubstringTwoDistinct("ccaabbbb")