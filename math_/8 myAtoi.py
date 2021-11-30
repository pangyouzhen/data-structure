import re


class Solution:
    def myAtoi(self, strs: str):
        regex_res = re.match("^(\s)*([+,-]?\d+)", strs)
        res = 0
        if regex_res:
            gr = int(regex_res.group())
            if gr > 2 ** 31 - 1:
                res = 2 ** 31 - 1
            elif gr < - 2 ** 31:
                res = -2 ** 31
            else:
                res = gr
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.myAtoi("42") == 42
    assert sol.myAtoi("4193 with words") == 4193
    assert sol.myAtoi("words and 987") == 0
    assert sol.myAtoi("-91283472332") == -2147483648
    assert sol.myAtoi("+") == 0
    assert sol.myAtoi("   +++") == 0
    assert sol.myAtoi("+1") == 1
    assert sol.myAtoi("+-2") == 0
    assert sol.myAtoi("-") == 0
    assert sol.myAtoi("   -42") == -42
