class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        all_area = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        inter_area = 0
        if ay1 >= by2 or ax1 >= bx2 or bx1 >= ax2 or by1 >= ay2:
            return all_area - inter_area
        x = [ax1,ax2,bx1,bx2]
        x.sort()
        y = [ay1,ay2,by1,by2]
        y.sort()
        print(x)
        print(y)
        return all_area - (x[2] - x[1]) * (y[2] - y[1])