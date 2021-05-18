class Solution:
    def judgeCircle(self, moves: str) -> bool:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # 上，左，下，右
        start = [0, 0]
        for i in moves:
            if i == "U":
                start = [start[0] + directions[0][0], start[1] + directions[0][1]]
            elif i == "D":
                start = [start[0] + directions[2][0], start[1] + directions[2][1]]
            elif i == "L":
                start = [start[0] + directions[1][0], start[1] + directions[1][1]]
            elif i == "R":
                start = [start[0] + directions[3][0], start[1] + directions[3][1]]
        return start == [0, 0]


if __name__ == '__main__':
    moves = "UD"
    sol = Solution()
    print(sol.judgeCircle(moves))
    moves = "LL"
    sol = Solution()
    print(sol.judgeCircle(moves))
    moves = "RLUURDDDLU"
    print(sol.judgeCircle(moves))
