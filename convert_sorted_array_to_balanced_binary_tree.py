class Solution:
    def sortedArrayToBST(self, nums):
        return self.convert_array(nums, 0, len(nums) -1)

    def convert_array(self, nums, left, right):
        if right < left:
            return None
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.convert_array(nums, left, mid - 1)
        node.right = self.convert_array(nums, mid + 1, right)
        return node
