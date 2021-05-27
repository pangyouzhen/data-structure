import pysnooper


class Solution:
    @pysnooper.snoop()
    def hammingDistance(self, x: int, y: int) -> int:
        a = bin(x).replace("0b", "")
        b = bin(y).replace("0b", "")
        res = 0
        for i, v in zip(a, b):
            if i != v:
                res += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingDistance(1, 4))
