class Solution:
    def maxDepth(self, s: str) -> int:
        if len(s) == 1:
            return 0
        res = [False] * (len(s))
        if s[0] == "(":
            res[0] = 1
        else:
            res[0] = 0
        for i in range(1, len(s)):
            if s[i] == "(":
                res[i] = res[i - 1] + 1
            elif s[i] == ")":
                res[i] = res[i - 1] - 1
            else:
                res[i] = res[i - 1]
        return max(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxDepth("(1)+((2))+(((3)))"))
