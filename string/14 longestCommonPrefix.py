from typing import List


class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        else:
            element_length = min(map(len, strs))
            i = 0
            default_value = []
            while (i < element_length):
                t = set(map(lambda x: x[i], strs))
                if len(t) == 1:
                    default_value.append(''.join(t))
                    i = i + 1
                else:
                    break
            if len(default_value) == 0:
                return ""
            else:
                return "".join(default_value)


if __name__ == '__main__':
    sol = Solution()
    res = sol.longestCommonPrefix([])
    print(res)
# 1. for循环这个list，list中的每一个元素从第一个位置开始匹配  if strs[0][1] == strs[1][1] == ... = strs[i][1]:
# 这样想比较麻烦，可以考虑，简化问题 -> 两个如何判断公共前缀，然后使用reduce 函数解决
#
from functools import reduce


class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        def twoCommonPrefix(fst: str, sed: str) -> str:
            cur = 0
            t = min(len(fst), len(sed))
            res = ""
            while cur < t:
                if fst[cur] == sed[cur]:
                    res += fst[cur]
                else:
                    return res
                cur += 1
            return res

        return reduce(twoCommonPrefix, strs)
