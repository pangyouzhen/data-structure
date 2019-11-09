import string
from itertools import product


class Solution:
    def titleToNumber(self, s: str) -> int:
        letters = string.ascii_uppercase
        letters_list = list(letters)
        letters_product = product(letters_list, letters_list)
        for i in letters_product:
            letters_list.append(i)
        result = list(map(lambda x: ''.join(x), letters_list))
        return result.index(s) + 1


if __name__ == '__main__':
    sol = Solution()
    # assert sol.titleToNumber("A") == 1
    print(sol.titleToNumber("A"))
