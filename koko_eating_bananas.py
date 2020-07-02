class Solution:
    def minEatingSpeed(self, piles, H):
        left = 1
        right = max(piles)
        min_k = float('inf')

        while left <= right:
            mid = (left + right) // 2
            hours = self.search(piles, mid)
            if hours > H:
                left = mid + 1
            else:
                right = mid - 1
                min_k = min(min_k, mid)


        return min_k

    def search(self, piles, k):
        hours = 0
        for pile in piles:
            hours += pile // k
            if pile % k != 0:
                hours += 1
        return hours


s = Solution()
print(s.minEatingSpeed([30,11,23,4,20], 6))
