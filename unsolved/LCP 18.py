from typing import List


class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        pass


if __name__ == '__main__':
    # staple = [10, 20, 5]
    # drinks = [5, 5, 2]
    # x = 15
    # staple = [6, 1, 9, 2, 9, 9, 3, 4]
    # drinks = [2, 7, 10, 2, 9, 2, 1, 3]
    # x = 2
    staple = [2, 1, 1]
    drinks = [8, 9, 5, 1]
    x = 9
    sol = Solution()
    print(sol.breakfastNumber(staple, drinks, x))
