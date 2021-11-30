import pysnooper


class Solution:
    @pysnooper.snoop()
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")

if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingDistance(1, 4))
