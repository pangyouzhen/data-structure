from typing import List


class Solution():
    # todo
    def stoneGameIX(self, stones: List[int]) -> bool:
        t = [i for i in stones if i%3 != 0]

if __name__ == "__main__":
    func = Solution().stoneGameIX
    nums = [5, 1, 2, 4, 3]
    print(func(nums))
