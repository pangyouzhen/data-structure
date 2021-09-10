from typing import List


class Solution:
    def __init__(self):
        self.letter_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.all_ans = []

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.letterCombinations_memo(digits, 0, "")
        return self.all_ans

    def letterCombinations_memo(self, digits, ind, one_ans):
        if ind == len(digits):
            self.all_ans.append(one_ans)
            return
        c = digits[ind]
        letter = self.letter_dict[c]
        for i in range(len(letter)):
            self.letterCombinations_memo(digits, ind + 1, one_ans + letter[i])


if __name__ == '__main__':
    digits = "23"
    out = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    func = Solution().letterCombinations
    print(func(digits))
