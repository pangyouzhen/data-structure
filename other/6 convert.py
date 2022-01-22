from math import ceil
from tokenize import group
from typing import List


class Solution():
    # 直接采用模拟的方法
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * numRows
        curRow = 0
        goingDown = False
        for c in s:
            rows[curRow] += c
            if curRow == 0 or curRow == numRows -1:
                goingDown = not goingDown
            if goingDown is True:
                curRow += 1 
            else:
                curRow += -1
        return "".join(rows)
            

if __name__ == "__main__":
    func = Solution().convert
    s = "PAYPALISHIRING"
    numRows = 2 
    print(func(s, numRows))
