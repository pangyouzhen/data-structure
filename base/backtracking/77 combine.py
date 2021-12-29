from typing import List, Any
from pysnooper import snoop


class Solution:
    def __init__(self):
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or k > n:
            return []
        self.combine_memo(n, k, 1, [])
        return self.res

    def combine_memo(self, n: int, k: int, start: int, one_ans: List[int]):
        # 纵向，因为是取两个元素，所以终止条件是长度
        if len(one_ans) == k:
            self.res.append(one_ans[:])
            print("--------------------")
            return
        # 横向遍历，for循环
        for i in range(start, n + 1):
            print(f"for i in range({start, n + 1})")
            # 这里次数为什么变成了n - (k - len(c)) + 2
            # for i in range(start, n - (k - len(one_ans)) + 2):
            one_ans.append(i)
            self.combine_memo(n, k, i + 1, one_ans)
            one_ans.pop()
        return

    #  python 内置的排列和组合
    def builtin_combinations(self, n: Any, k: int):
        from itertools import combinations
        return list(combinations(range(1, n + 1), k))


if __name__ == '__main__':
    sol = Solution()
    print(sol.combine(4, 2))
    # print(sol.builtin_combinations(4, 2))
