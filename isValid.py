import re


class Solution:
    def isValid(self, s):
        ls = list(s)
        if len(s) > 0:
            previous = ls[:int(len(ls) / 2)]
            end = ls[int(len(ls) / 2):]
            if previous == end:
                return True
            elif len(previous) != len(end):
                return False
            elif re.search("\(\)|\[\]|{}", s):
                return True
            else:
                return False
        else:
            return True


if __name__ == '__main__':
    sol = Solution()
    res = sol.isValid("([]}")
    print(res)
