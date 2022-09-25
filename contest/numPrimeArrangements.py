import math


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def is_prime(n):
            if n == 1:
                return False
            if n == 2:
                return True
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

        prime_nums = 0
        for i in range(1, n + 1):
            if is_prime(i):
                prime_nums += 1

        not_prime_nums = n - prime_nums

        return (math.factorial(prime_nums) * math.factorial(not_prime_nums)) % (10 ** 9 + 7)
