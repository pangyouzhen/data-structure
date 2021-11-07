from typing import List


class Solution:
    def maxPower(self, s):
        t = 0
        v = None
        curr_val = 0
        for i in s:
            if i != v:
                v = i
                curr_val = 1
            else:
                curr_val += 1
            if curr_val > t:
                t = curr_val
        return t


if __name__ == '__main__':
    s = "leetcode"
    sol = Solution()
    print(sol.maxPower(s))
