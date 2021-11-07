from typing import List


class LargerNumKey(str):
    def __lt__(self, other):
        return self + other > other + self
#     这里的相加方法是继承的str的__add__的函数


print(LargerNumKey('1') < LargerNumKey('0'))
print(LargerNumKey("100") < LargerNumKey("10"))

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
