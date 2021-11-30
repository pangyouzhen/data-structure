from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        t = Counter(s)
        uniq = set(t.values())
        if len(uniq) == 1:
            return True
        return False


if __name__ == '__main__':
    s = "abacbc"
    sol = Solution()
    print(sol.areOccurrencesEqual(s))
