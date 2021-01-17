from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        start =coordinates[:2]
        y_minus = coordinates[1][1] - coordinates[0][1]
        x_minus = coordinates[1][0] - coordinates[0][0]
        if x_minus == 0:
            for i in coordinates[2:]:
                if i[0] != coordinates[0][0]:
                    return False
            return True
        else:
            a = y_minus / x_minus
            b = coordinates[0][1] - a * coordinates[0][0]
            for i in coordinates[2:]:
                if (a * i[0] + b) != i[1]:
                    # print(a,b)
                    # print(i)
                    return False
            return True