class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
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
        all_ans = []
        def dfs(digits,ind,one_ans):
            if ind == len(digits):
                all_ans.append("".join(one_ans))
                return
            c = digits[ind]
            letter = letter_dict[c]
            for i in letter:
                one_ans.append(i)
                dfs(digits,ind+1,one_ans)
                one_ans.pop()
        one_ans = []
        dfs(digits,0,one_ans)
        return all_ans