from typing import List, Any


class Solution:

    def combine(self, n: int, k: int):
        global res
        res = []
        if n <= 0 or k <= 0 or k > n:
            return res
        c = []
        self.combine_memo(n, k, 1, c)
        return res

    def combine_memo(self, n: int, k: int, start: int, c):
        if len(c) == k:
            #  这里为什么 append(c[:]) 是正确的，但是append(c)最后返回的结果是 [[],[],[],...]
            #  这里 append c是append的c的指针，所有的都是指的同一个对象，最后回溯的时候c被清空了，所以所有的res的值就变成了[[],[],[]]
            res.append(c[:])
            # res.append(c)
            return
        # for i in range(start, n + 1):
        # 这里次数为什么变成了n - (k - len(c)) + 2
        for i in range(start, n - (k - len(c)) + 2):
            print(f"{start = },{i = },{n - (k - len(c)) + 2 = }")
            c.append(i)
            # 这里为什么是i+1
            self.combine_memo(n, k, i + 1, c)
            c.pop()
        print("-------------")
        return

    # 因为是两个两个元素就终止，可以理解上面的递归其实
    # for i in range(1, 5):
    #     for j in range(i, 5):
    #         print(j)
    # 1, 2, 3, 4
    # 2, 3, 4
    # 3, 4
    # 4
    # print("____")

    # start = 1, i = 1, n - (k - len(c)) + 2 = 4
    # start = 2, i = 2, n - (k - len(c)) + 2 = 5  这里 for i in range(2,5), i=2 break
    # start = 2, i = 3, n - (k - len(c)) + 2 = 5  这里 for i in range(2,5), i=3 break
    # start = 2, i = 4, n - (k - len(c)) + 2 = 5  这里 for i in range(2,5), i=2 break
    # -------------
    # start = 1, i = 2, n - (k - len(c)) + 2 = 4
    # start = 3, i = 3, n - (k - len(c)) + 2 = 5
    # start = 3, i = 4, n - (k - len(c)) + 2 = 5
    # -------------
    # start = 1, i = 3, n - (k - len(c)) + 2 = 4
    # start = 4, i = 4, n - (k - len(c)) + 2 = 5
    # -------------
    # -------------

    #  python 内置的排列和组合
    def builtin_combinations(self, n: Any, k: int):
        from itertools import combinations
        return list(combinations(range(1, n + 1), k))


if __name__ == '__main__':
    sol = Solution()
    print(sol.combine(4, 2))
    # print(sol.builtin_combinations(4, 2))
