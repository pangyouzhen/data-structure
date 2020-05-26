from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        t = Counter(s)
        m = [v for v in t.values()]
        even = [i for i in m if i % 2 == 0]
        odd = [i for i in m if i % 2 != 0]
        odd.sort()
        if len(odd) > 0:
            fst = odd[-1]
        else:
            fst = 0
        return sum(even) + fst


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome("bananas"))

# "bananas"
