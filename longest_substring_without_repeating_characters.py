class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        left = 0
        right = 0
        hashset = set()
        res = 0

        while right < len(s):
            if s[right] not in hashset:
                hashset.add(s[right])
                res = max(res, len(hashset))
                right += 1
            else:
                hashset.remove(s[left])
                left += 1

        return res

s = Solution()
s.lengthOfLongestSubstring("pwwkew")