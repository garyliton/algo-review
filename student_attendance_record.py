class Solution:
    def checkRecord(self, s: str):
        if s.count('A') > 1:
            return False

        if 'LLL' in s:
            return False

        return True
