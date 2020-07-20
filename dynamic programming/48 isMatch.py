from pprint import pprint


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rows = len(p) + 1
        cols = len(s) + 1
        table = [[False] * cols for i in range(rows)]
        table[0][0] = True
        if p.startswith("*"):
            table[1] = [True] * cols
        for m in range(1, rows):
            path = False
            for n in range(1, cols):
                if p[m - 1] == "*":
                    if table[m - 1][0] == True:
                        table[m] = [True] * cols
                    if table[m - 1][n]:
                        path = True
                    if path:
                        table[m][n] = True
                elif p[m - 1] == "?" or p[m - 1] == s[n - 1]:
                    table[m][n] = table[m - 1][n - 1]
        pprint(table)
        return table[rows - 1][cols - 1]


# dp = [
#  [True, False, False, False, False, False],
#  [False, True, False, False, False, False],
#  [False, True, True, True, True, True],
#  [False, False, False, False, False, True]

if __name__ == '__main__':
    s = "adceb"
    p = "a*b"
    sol = Solution()
    print(sol.isMatch(s, p))
