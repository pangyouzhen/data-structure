from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        allowed_set = set(allowed)
        for i in words:
            if set(i).union(allowed_set) == allowed_set:
                res += 1
        return res


if __name__ == '__main__':
    allowed = "cad"
    words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
    sol = Solution()
    print(sol.countConsistentStrings(allowed, words))
