class Solution:
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        longest_seq = 0

        for num in nums:
            if num - 1 not in nums_set:
                current_num = num
                current_seq = 0
                while current_num in nums_set:
                    current_seq += 1
                    current_num += 1
                longest_seq = max(current_seq, longest_seq)

        return longest_seq
