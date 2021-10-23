from typing import List
from math import sqrt


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        """
        这就是个数学问题  x*y = t 求 min(x-y) 变量换元得到 min(x*(t/x))
        -> min(x^2 - t)) -> 导数就为2x，左边单减。右边单增 -> 与横坐标的交点
        为 sqrt(x), 只要找到sqrt右侧的第一个使得x，y均为整数的点即可
        """
        mid = sqrt(area)
        a = mid
        while int(a) != float(a):
            mid = int(mid) + 1
            a = area / mid
        return [int(mid), int(a)]


if __name__ == '__main__':
    area = 5
    sol = Solution().constructRectangle
    print(sol(area))
