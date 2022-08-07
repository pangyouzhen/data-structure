from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        a = 0
        amount = list(filter(lambda x: x > 0, amount))
        while len(amount) > 1:
            amount.sort()
            amount[0] -= 1
            amount[-1] -= 1
            amount = list(filter(lambda x: x > 0, amount))
            a += 1
        return a+sum(amount)


if __name__ == "__main__":
    func = Solution().fillCups
    