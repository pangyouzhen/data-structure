from typing import List


class Solution:
    # 五子连棋
    def judge(self, arr: List[List[int]], flag: int, x: int, y: int) -> bool:
        """
        # 这个先不计算 x，y越界的情况
        arr: 当前棋盘的状态
        flag: 当前子是黑还是白,0,1
        x: 当前所放x位置
        y: y位置
        :rtype: bool
        """
        # 五子连棋主要判断四个方向水平
        # 竖直方向
        vertical_nums = 0
        for vertical in range(-4, 4):
            if arr[x][y - vertical] == flag:
                vertical_nums += 1
            else:
                vertical_nums = 0
            if vertical_nums >= 5:
                return True
        # 水平方向
        horizontal_nums = 0
        for horizontal in range(-4, 4):
            if arr[x - horizontal][y] == flag:
                horizontal_nums += 1
            else:
                horizontal_nums = 0
            if horizontal_nums >= 5:
                return True
        # 左上-右下对角线
        left_up_diag_nums = 0
        for left_up_diag in range(-4, 4):
            if arr[x - left_up_diag][y + left_up_diag] == flag:
                left_up_diag_nums += 1
            else:
                left_up_diag_nums = 0
            if left_up_diag_nums >= 5:
                return True
        # 左下-右上对角线
        left_down_diag_nums = 0
        for left_down_diag in range(-4, 4):
            if arr[x - left_down_diag][y - left_down_diag] == flag:
                left_down_diag_nums += 1
            else:
                left_down_diag_nums = 0
            if left_down_diag_nums >= 5:
                return True
        return False

    # def contain_continuous(self, line: List[int], flag: int) -> bool:
    #     """
    #      判断一个序列中是否存在5个连续的flag
    #      [0,1,1,0,1,0,1,0,0,1]
    #     """
    #     nums = 0
    #     for i in line:
    #         if i == flag:
    #             nums += 1
    #         else:
    #             nums = 0
    #         if nums >= 5:
    #             return True
    #     return False


if __name__ == '__main__':
    sol = Solution()
    # print(sol.judge())
    # print(sol.contain_continuous([1, 0, 1, 1, 0, 0, 1, 0, 0], 0))
