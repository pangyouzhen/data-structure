import string


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s = string.ascii_uppercase
        s_dic = {v: i + 1 for i, v in enumerate(s)}
        print(s_dic)
        res = 0
        for i, v in enumerate(columnTitle):
            var = s_dic[v] + 26 ** i - 1
            res += var
        return res


if __name__ == '__main__':
    columnTitle = "ZY"
    func = Solution().titleToNumber
    print(func(columnTitle))
