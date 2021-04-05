from typing import List


class Solution:
    def reverseWords(self, s):
        ts = s.split()
        return " ".join(ts[::-1])


if __name__ == '__main__':
    s = "  hello world!  "
    sol = Solution()
    print(sol.reverseWords(s))
