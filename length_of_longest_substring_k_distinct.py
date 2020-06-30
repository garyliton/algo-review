class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        left = right = 0
        hash_table = {}
        max_len = 0

        while right < len(s):
            if len(hash_table) < k + 1:
                hash_table[s[right]] = right
                right += 1

            if len(hash_table) == k + 1:
                min_idx = min(hash_table.values())
                hash_table.pop(s[min_idx])
                left = min_idx + 1

            max_len = max(max_len, right - left)

        return max_len

s = Solution()
print(s.lengthOfLongestSubstringKDistinct("aa", 1))
