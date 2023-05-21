from typing import List


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s = set()
        for x in nums:
            i = 2
            while i * i <= x:
                if x % i == 0:
                    s.add(i)
                    x //= i
                    while x % i == 0:
                        x //= i
                i += 1
            if x > 1:
                s.add(x)
        return len(s)


if __name__ == "__main__":
    nums = [2, 4, 3, 7, 10, 6]
    func = Solution().distinctPrimeFactors
    print(func(nums))
