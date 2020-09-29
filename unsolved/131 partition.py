from typing import List
from collections import Counter

# TODO
class Solution:
    def __init__(self):
        self.res = []

    def partition(self, s: str) -> List[List[str]]:
        self.partition_memo(s, 0, [])
        return self.res

    def partition_memo(self, s, start, one_ans):
        if start == len(s):
            self.res.append(one_ans[:])
            return
        for i in range(start, len(s)):
            one_ans.append(s[i])
            self.partition_memo(s, i + 1, one_ans)
            one_ans.pop()
        return

    # def check_pali(self):


if __name__ == '__main__':
    t = "aab"
    sol = Solution()
    print(sol.partition(t))
