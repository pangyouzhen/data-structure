from typing import List

from itertools import permutations


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits = [str(i) for i in digits]
        nums = []
        for i in permutations(digits, 3):
            s = ''.join(list(i))
            if not s.startswith("0"):
                j = int(s)
                if j % 2 == 0:
                    nums.append(j)
        nums = list(set(nums))
        nums.sort()
        return nums


if __name__ == '__main__':
    a = [2, 1, 3, 0]
    func = Solution().findEvenNumbers
    print(func(a))
