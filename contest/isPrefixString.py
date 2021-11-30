from typing import List
import pysnooper


class Solution:
    @pysnooper.snoop()
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        text = ""
        for w in words:
            text = text + w
            if s == text:
                return True
        return False


if __name__ == '__main__':
    sol = Solution().isPrefixString
    s = "cccccccc"
    words = ["c", "c"]
    # words = ["cccccccccc"]
    print(sol(s, words))
