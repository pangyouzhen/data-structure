from functools import cache
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ret = list()
        ans = list()

        @cache
        def isPalidrome(i: int, j: int) -> int:
            if i > j:
                return 1
            return isPalidrome(i + 1, j - 1) if s[i] == s[j] else -1

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return
            for j in range(i, n):
                if isPalidrome(i, j) == 1:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        isPalidrome.cache_clear()
        return ret


if __name__ == '__main__':
    res = [
        ["aa", "b"],
        ["a", "a", "b"]
    ]
    t = "aab"
    sol = Solution()
    print(sol.partition(t))
    # assert sol.partition(t) == res
