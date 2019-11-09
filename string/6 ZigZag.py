class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows > len(s):
            return s
        zigzag = ["" for x in range(numRows)]

        row, step = 0, 1
        for crct in s:
            # 这里用list用+=是不清楚的，以前只是用过设定好list长度进行赋值
            zigzag[row] += crct

            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1

            row += step

        return ''.join(zigzag)


if __name__ == '__main__':
    sol = Solution()
    assert sol.convert("PAYPALISHIRING", numRows=3) == "PAHNAPLSIIGYIR"
    assert sol.convert("PAYPALISHIRING", numRows=4) == "PINALSIGYAHRPI"
