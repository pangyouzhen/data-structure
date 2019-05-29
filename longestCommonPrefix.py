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
# for循环这个list，list中的每一个元素从第一个位置开始匹配  if strs[0][1] == strs[1][1] == ... = strs[i][1]:
