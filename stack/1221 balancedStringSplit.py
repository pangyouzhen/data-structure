from collections import defaultdict


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        a = defaultdict(int)
        res = 0 
        for ind, i in enumerate(s):
            a["%s" % i] += 1
            if a["R"] != 0 and a["R"] == a["L"]:
                res += 1
                # a = defaultdict(int)
        return res


if __name__ == '__main__':
    s = "RLRRLLRLRL"
    sol = Solution()
    print(sol.balancedStringSplit(s))
