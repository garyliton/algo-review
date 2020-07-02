class Solution:
    def countPrimes(self, n: int):
        primes = [True for i in range(n)]

        i = 2
        while i * i < n:
            if primes[i]:
                j = i
                while i * j < n:
                    primes[i * j] = False
                    j += 1
            i += 1
        count = 0
        for is_prime in primes[2:]:
            if is_prime:
                count += 1
        return count


s = Solution()
print(s.countPrimes(2))
