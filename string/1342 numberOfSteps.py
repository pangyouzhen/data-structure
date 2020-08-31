class Solution:
    def numberOfSteps(self, num: int) -> int:
        global res
        res = 0
        res = self.numberOfSteps_memo(num, 0)
        return res

    def numberOfSteps_memo(self, num, t):
        if num == 0:
            return t
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        res = res +1
        t = self.numberOfSteps_memo(num, t + 1)
        return t


if __name__ == '__main__':
    num = 14
    sol = Solution()
    print(sol.numberOfSteps(14))
