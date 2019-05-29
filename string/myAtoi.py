import re


class Solution:
    def myAtoi(self, strs):
        res = []
        a = 0
        while (a < len(strs)):
            if not strs[a].isdigit() and strs[a] != "+" and strs[a] != "-":
                break
            else:
                if strs[a].isdigit() and (a + 1) < len(strs) and strs[a + 1].isdigit():
                    res.append(str(strs[a]))
                elif (strs[a] == "+" or strs[a] == "-") and (a + 1) < len(strs) and strs[a + 1].isdigit():
                    res.append(str(strs[a]))
                elif a + 1 == len(strs):
                    res.append(str(strs[a]))
                else:
                    break
            a = a + 1
        if "+" in res and "-" in res:
            return 0
        else:
            res = list(filter(lambda x: x != "+", res))
            if len(res) == 0:
                return 0
            elif len(res) == 1 and "-" in res:
                return 0
            elif int(''.join(res)) > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif int(''.join(res)) < - 2 ** 31:
                return -2 ** 31
            else:
                return int(''.join(res))
        # strs = re.sub(" ", "", strs)


# print(strs[0])
# regex_res = re.search("-{0,1}\d+", strs)
# if regex_res:
#     if strs[0] == "-" or strs[0] == "+" or strs[0].isdigit():
#         gr = int(regex_res.group())
#         if gr > 2 ** 31 - 1:
#             return 2 ** 31 - 1
#         elif gr < - 2 ** 31:
#             return -2 ** 31
#         else:
#             return gr
#     else:
#         return 0
# else:
#     return 0


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
    assert sol.myAtoi("0-1") == 0
