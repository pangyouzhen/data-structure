from typing import List


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


if __name__ == '__main__':
    sol = Solution()
    assert sol.largestNumber([10, 2]) == "210"
    print(sol.largestNumber([3, 30, 34, 5, 9]))
    assert sol.largestNumber([3, 30, 34, 5, 9]) == "9534330"


sorted(map(str, [3, 30, 34, 5, 9]), key=LargerNumKey)