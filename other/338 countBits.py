from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        return [bin(i).count("1") for i in range(0, num + 1)]


if __name__ == '__main__':
    sol = Solution()
    print(sol.countBits(5))
