class Solution:
    # 五子连棋
    # todo 需要验证
    def judge(self, arr, flag, x, y):
        """
        arr: 当前棋盘的状态
        flag: 当前子是黑还是白,0,1
        x: 当前所放x位置
        y: y位置
        :rtype: bool
        """
        # 五子连棋主要判断四个方向水平，竖直
        # 竖直方向
        vertical = [str(arr[x][y - i]) for i in range(-4, 4)]
        if self.contain_continuous(vertical, flag):
            return True
        # 水平方向
        horizontal = [str(arr[x - i][y]) for i in range(-4, 4)]
        if self.contain_continuous(horizontal, flag):
            return True
        # 左上-右下对角线
        left_up_diag = [str(arr[x - i][y + i]) for i in range(-4, 4)]
        if self.contain_continuous(left_up_diag, flag):
            return True
        # 左下-右上对角线
        left_down_diag = [str(arr[x - i][y - i]) for i in range(-4, 4)]
        if self.contain_continuous(left_down_diag, flag):
            return True
        return False

    def contain_continuous(self, arr, flag):
        """
         判断一个序列中是否存在5个连续的flag
         [0,1,1,0,1,0,1,0,0,1]
        """
        val = "".join(arr)
        if flag == "0" or flag == 0:
            for i in val.split("1"):
                if len(i) == 5:
                    return True
        else:
            for i in val.split("0"):
                if len(i) == 5:
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    # print(sol.judge())
    print(sol.contain_continuous(["1", "1", "1", "1", "0", "0", "0", "0", "0"], 0))
