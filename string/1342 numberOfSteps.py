class Solution:
    def numberOfSteps(self, num: int) -> int:
        global res
        res = {"res": 0}
        #  这里不能用整数，整数不起作用的原因是因为有歧义的，
        #  不能确定是否是 local变量是赋值的还是global变量，local变量的优先级高于global所以不能这样用
        self.numberOfSteps_memo(num)
        return res["res"]

    def numberOfSteps_memo(self, num):
        if num == 0:
            return
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        res["res"] += 1
        self.numberOfSteps_memo(num)
        return


if __name__ == '__main__':
    num = 14
    sol = Solution()
    print(sol.numberOfSteps(14))
