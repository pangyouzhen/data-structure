
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
        for i in range(start, n + 1):
            c.append(i)
            self.combine_memo(n, k, i + 1, c)
            c.pop()
        return


if __name__ == '__main__':
    sol = Solution()
    print(sol.combine(4, 2))
