class Solution:
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        try:
            return haystack.index(needle)
        except ValueError:
            return -1


if __name__ == '__main__':
    sol = Solution()
    res = sol.strStr("mississippi", "deissip")
    print(res)
