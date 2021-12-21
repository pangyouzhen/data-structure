class Solution:
    def dayOfYear(self, date: str) -> int:
        a = [1, 3, 5, 7, 8, 10, 12]
        year, month, day = date.split("-")
        month = int(month)
        month -= 1
        day = int(day)
        res = 0
        while month > 0:
            if month in a:
                res += 31
            elif month == 2:
                if self.is_leap_year(year):
                    res += 29
                else:
                    res += 28
            else:
                res += 30
            month -= 1
        res += day
        return res

    def is_leap_year(self, year: str):
        year = int(year)
        red = year / 100
        if int(red) == red:
            t = year / 400
            if int(t) == t:
                return True
        else:
            t = year / 4
            if int(t) == t:
                return True
        return False


if __name__ == '__main__':
    func = Solution().dayOfYear
    print(func("2019-01-09"))
