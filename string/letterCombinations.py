from typing import List
import itertools
from functools import reduce


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits:
            letter_dict = {
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz",
            }
            digits_ls = list(digits)
            letter_ls = list(map(lambda x: list(letter_dict["{}".format(x)]), digits_ls))
            product = lambda x, y: [''.join(list(y)) for y in itertools.product(x, y)]
            res = reduce(product, letter_ls)
            return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCombinations("23"))
