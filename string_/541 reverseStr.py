from typing import List


class Solution(object):
    def reverseStr(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2 * k):
            a[i:i + k] = reversed(a[i:i + k])
        return "".join(a)


if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    sol = Solution()
    print(sol.reverseStr(s, k))
