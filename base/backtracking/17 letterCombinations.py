from typing import List
from pysnooper import snoop


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

    @snoop()
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.letterCombinations_memo(digits, 0, "")
        return self.all_ans

    @snoop()
    # digits="23",ind=0,one_ans=[]
    # 这里最终返回的是-> List[str]，所以每一个元素应该是str,所以one_ans应该是str
    def letterCombinations_memo(self, digits: str, ind: int, one_ans: str) -> None:
        if ind == len(digits):
            self.all_ans.append(one_ans)
            return
        c = digits[ind]
        letter = self.letter_dict[c]
        for i in range(len(letter)):
            one_ans += letter[i]
            self.letterCombinations_memo(digits, ind + 1, one_ans)
            # 因为one_ans为str，没有-= 方法，只能这样回溯
            one_ans = one_ans[:-1]


if __name__ == '__main__':
    digits = "23"
    # out = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    # 其实整体拆开来看就是n个for 循环，对于这个题目的23来讲，就是for i in list("abc"): for j in list("def")"
    # 但是对于多个数字来讲就不合适了比如 "23455" 就是5层循环
    func = Solution().letterCombinations
    print(func(digits))
