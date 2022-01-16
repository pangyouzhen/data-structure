from pysnooper import snoop


class Solution:
    # @snoop()
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target != 1:
            if target % 2 == 1 and maxDoubles != 0:
                target -= 1
            elif maxDoubles > 0:
                target = target / 2
                maxDoubles -= 1
            elif maxDoubles == 0:
                res += target - 1
                return int(res)
            res += 1
        return int(res)


if __name__ == '__main__':
    print(Solution().minMoves(10, 4))
