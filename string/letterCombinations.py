from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
        pass


if __name__ == '__main__':
    sol = Solution()
    sol.letterCombinations("23")
