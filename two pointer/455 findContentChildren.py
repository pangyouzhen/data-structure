from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        g.sort()
        s.sort()
        left = 0
        right = 0
        while left < len(g) and right < len(s):
            if g[left] <= s[right]:
                left += 1
                right += 1
                result += 1
            else:
                right += 1
        return result


if __name__ == '__main__':
    sol = Solution()
    assert sol.findContentChildren([1, 2, 3], [1, 1]) == 1
    assert sol.findContentChildren([11, 22], [1, 2, 3, 33, 22]) == 2
    assert sol.findContentChildren([10, 9, 8, 7], [5, 6, 7, ]) == 1
