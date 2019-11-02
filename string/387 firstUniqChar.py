class Solution:
    def firstUniqChar(self, s):
        s_lst = list(s)
        a = {}
        for i, v in enumerate(s_lst):
            if v not in a.keys():
                a['%s' % v] = 1
            else:
                a["%s" % v] = a["%s" % v] + 1
        for i, v in a.items():
            if v == 1:
                return s_lst.index(i)
        return -1


if __name__ == '__main__':
    sol = Solution()
    res = sol.firstUniqChar("loveleetcode")
    print(res)
