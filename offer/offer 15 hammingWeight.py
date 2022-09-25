from typing import List


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


if __name__ == "__main__":
    func = Solution().hammingWeight
    n = 128
    print(func(n))
