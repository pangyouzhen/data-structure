class Solution:
    # todo
    def judge(self, arr, flag, x, y):
        """
        arr: 当前棋盘的状态
        flag: 当前子是黑还是白
        x: 当前所放x位置
        y: y位置
        :rtype: bool
        """
        directions = [-1, 1, 0]
        direct = []
        for i in directions:
            for j in directions:
                if i == j == 0:
                    direct.append((i, j))
        print(direct)


if __name__ == '__main__':
    sol = Solution()
    print(sol.judge())
