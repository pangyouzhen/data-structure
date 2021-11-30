class Solution:
    def totalMoney(self, n: int) -> int:
        m = n // 7
        t = n % 7
        last_day = n - m * 7
        last_money = (m + 1 + (last_day + m)) * t / 2
        for i in range(int(m)):
            money = (1 + i + 7 + i) * 7 / 2
            last_money += money
        return int(last_money)


if __name__ == '__main__':
    n = 20
    sol = Solution()
    print(sol.totalMoney(n))
