class Solution:
    def numWays(self, s: str) -> int:
        MODULO = 1000000007

        ones = list()
        n = len(s)
        for i, digit in enumerate(s):
            if digit == "1":
                ones.append(i)

        m = len(ones)
        if m % 3 != 0:
            return 0

        if m == 0:
            ways = (n - 1) * (n - 2) // 2
            return ways % MODULO
        else:
            index1, index2 = m // 3, m // 3 * 2
            count1 = ones[index1] - ones[index1 - 1]
            count2 = ones[index2] - ones[index2 - 1]
            ways = count1 * count2
            return ways % MODULO


if __name__ == '__main__':
    s = "010101"
    sol = Solution()
    print(sol.numWays(s))
