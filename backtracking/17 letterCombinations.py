#  递归，树形结构
class Solution:
    def letterCombinations(self, digits):
        global letter_dict, res
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
        res = []
        self.letterCombinations_rec(digits, 0, "")
        return res

    def letterCombinations_rec(self, digits, index_val, char):
        # print(f"{digits=},{index_val,}{char=}")
        if index_val == len(digits):
            res.append(char)
            return
        # 这个感觉必须要用两层循环的？,一个循环在 递归中消解了
        # if digits:
        #     for i in chain("", digits):
        #         if i:
        #             res.append(letter_dict[i] + self.letterCombinations_rec(digits[i:]))
        #         else:
        #             res = self.letterCombinations_rec(digits[i:])
        c = digits[index_val]
        letter = letter_dict[c]
        for i in range(len(letter)):
            # print(letter[i])
            self.letterCombinations_rec(digits, index_val + 1, char + letter[i])
        return


# self.letterCombinations_rec("23", 0, "")
# self.letterCombinations_rec("23", 1, "" + "a")
# self.letterCombinations_rec("23", 2, "a" + "d")
# append and return 把这一层的循环销毁了，
# self.letterCombinations_rec("23", 2,  "a" + "e")
# self.letterCombinations_rec("23", 2,  "a" + "f")
# return 语句把这一层的销毁
# self.letterCombinations_rec("23", 1, "" + "b")


if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCombinations("23"))
