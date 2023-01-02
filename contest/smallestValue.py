from functools import lru_cache


class Solution:
    @lru_cache
    def smallestValue(self, n: int) -> int:
        self.n = n
        all_prime = self.all_prime_func()
        if n in set(all_prime) or n == 4:
            return n
        k = 0
        while n not in set(all_prime) or n != 4:
            for t in all_prime:
                if n % t == 0:
                    k += t
                    n = int(n / t)
        k += t
        return self.smallestValue(k)

    @lru_cache
    def all_prime_func(self):
        k = (
            int(
                max(
                    self.n / 6,
                    (self.n - 1) / 6,
                    (self.n - 2) / 6,
                    (self.n - 3) / 6,
                    (self.n - 4) / 6,
                    (self.n - 5) / 6,
                )
            )
            + 1
        )
        self.all_prime = [2, 3, 5]
        for i in range(1,k):
            self.all_prime.append(6 * i + 1)
            self.all_prime.append(6 * i + 5)
        return self.all_prime


if __name__ == "__main__":
    sol = Solution()
    func = sol.smallestValue
    n = 15
    print(func(15))
    print(sol.all_prime)
