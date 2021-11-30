from typing import List

from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = None
        for a in A:
            c = Counter(a)
            if res is None:
                res = c
            else:
                #相当于依次执行and和赋值
                res &= c
        return list(res.elements())


if __name__ == '__main__':
    A = ["bella", "label", "roller"]
    sol = Solution()
    print(sol.commonChars(A))
