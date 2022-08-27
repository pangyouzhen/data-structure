from typing import List


class Solution:
    def knap(self, w: List[int], v: List[int], c: int):
        n = len(w)
        res = self.knap_memo(w, v, n - 1, c)
        return res

    def knap_memo(self, w: List[int], v: List[int], index: int, c: int):
        if c <= 0 or index < 0:
            return 0
        res = self.knap_memo(w, v, index - 1, c)
        if c >= w[index]:
            res = max(
                self.knap_memo(w, v, index - 1, c),
                self.knap_memo(w, v, index - 1, c - w[index]) + v[index]
            )
        return res


if __name__ == '__main__':
    w = [20, 30, 40, 50, 60]
    v = [20, 30, 44, 55, 60]
    c = 100
    func = Solution().knap
    print(func(w, v, c))
