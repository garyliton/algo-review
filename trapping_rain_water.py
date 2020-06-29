class Solution:
    def trap(self, height):
        if not height:
            return 0

        left = [height[0]]
        right_max = height[-1]
        count = 0

        for i in range(1, len(height)):
            left.append(max(height[i], left[i-1]))

        for i in range(len(height) - 2, 0, -1):
            right_max = max(height[i], right_max)
            count += min(left[i ], right_max) - height[i]


        return count

s = Solution()
s.trap([0,1,0,2,1,0,1,3,2,1,2,1])