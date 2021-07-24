class Solution:
    def maximumTime(self, time: str) -> str:
        res = ""
        hour = time[:2]
        minus = time[3:]
        fill_num = hour.count("?")
        minus_fill_num = minus.count("?")
        if fill_num == 0:
            res += hour
        elif fill_num == 2:
            res += "23"
        else:
            if hour[0] == "2":
                res += "23"
            elif hour[0] == "1":
                res += "19"
            elif hour[0] == "0":
                res += "09"
            if hour[0] == "?":
                if int(hour[1]) < 4:
                    res += "2"
                    res += hour[1]
                else:
                    res += "1"
                    res += hour[1]
        res += ":"
        if minus_fill_num == 1:
            if minus[0] == "?":
                res += "5"
                res += minus[1]
            else:
                res += minus[0]
                res += "9"
        elif minus_fill_num == 2:
            res += "59"
        else:
            res += minus
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumTime("2?:?0"))
