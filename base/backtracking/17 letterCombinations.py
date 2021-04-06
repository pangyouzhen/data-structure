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
        if index_val == len(digits):
            res.append(char)
            return
        c = digits[index_val]
        letter = letter_dict[c]
        for i in range(len(letter)):
            # print(letter[i])
            #  这里可以和树形结构共同思考
            self.letterCombinations_rec(digits, index_val + 1, char + letter[i])
        return



if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCombinations("23"))
