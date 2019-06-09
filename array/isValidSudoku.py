class Solution:
    def isValidSudoku(self, board):
        # rows
        rows = list(map(self.is_not_has_duplicate, board))

        return True

    def is_not_has_duplicate(self, nums):
        t = list(filter(lambda x: x != ".", nums))
        res = True
        if len(t) != len(tuple(t)):
            res = False
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.isValidSudoku( [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["9", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]) == False
    assert sol.is_not_has_duplicate(["8", "3", ".", ".", "7", ".", ".", ".", "."], ) == True
    print(sol.isValidSudoku(["8", "3", ".", ".", "7", ".", ".", ".", "."], ))
