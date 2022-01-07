class Solution:
    def maxDepth(self, s: str) -> int:
        m = 0
        res = 0
        for i, v in enumerate(s):
            if v == "(":
                res += 1
                if res > m:
                    m = res
            elif v == ")":
                res -= 1
        return m


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxDepth("1"))
