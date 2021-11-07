from collections import Counter


class Solution:
    def firstUniqChar(self, s):
        t = Counter(s)
        for i, v in enumerate(s):
            if t[v] == 1:
                return i
        return -1


if __name__ == '__main__':
    sol = Solution()
    res = sol.firstUniqChar("loveleetcode")
    print(res)
