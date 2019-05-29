class Solution:
    def isValidSudoku(self, board):
        # rows
        # rows = 0
        # while (rows < 9):
        #     res = []
        #     for v in board[rows]:
        #         if (v in res) and (v != "."):
        #             return False
        #         else:
        #             res.append(v)
        #     rows = rows + 1
        #
        # # columns
        # column = 0
        # while (column < 9):
        #     res = []
        #     # while (a < 9):
        #     columns_ = list(map(lambda x: x[column], board))
        #     for v in columns_:
        #         if (v in res) and (v != "."):
        #             return False
        #         else:
        #             res.append(v)
        #     column = column + 1
        # board[0][1],board[1][1],board[2][1]...

        #  grid
        grid = 0
        while (grid < 3):
            res = []
            v = board[grid * 3:grid * 3 + 3]
            grid_columns = list(map(lambda x: x[grid * 3, grid * 3 + 3], [v]))
            print(grid_columns)
            for v in grid_columns:
                if (v in res) and (v != "."):
                    return False
                else:
                    res.append(v)
            pass
        grid = grid + 1

        #
        return True


if __name__ == '__main__':
    sol = Solution()
    res = sol.isValidSudoku([
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["9", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ])
    print(res)
