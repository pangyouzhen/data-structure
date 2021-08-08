from typing import List
import pysnooper


class Solution:
    @pysnooper.snoop()
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        s = list(s)
        for i in range(len(words)):
            if s:
                w = words[i]
                w_s = "".join(s[:len(w)])
                if w != w_s:
                    return False
                else:
                    s = s[len(w):]
        if s:
            return False
        return True


if __name__ == '__main__':
    sol = Solution().isPrefixString
    s = "cccccccc"
    words = ["c", "c"]
    # words = ["cccccccccc"]
    print(sol(s, words))
