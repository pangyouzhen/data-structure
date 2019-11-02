class Solution:
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        elif len(haystack.split(needle)) > 1:
            if haystack.split(needle)[0] == "":
                return 0
            return len(haystack.split(needle)[0])
        else:
            return -1


if __name__ == '__main__':
    sol = Solution()
    res = sol.strStr("mississippi", "issip")
    print(res)
