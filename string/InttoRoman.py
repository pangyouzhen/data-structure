class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_ls = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "III", "II", "I"]
        value_ls = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 3, 2, 1]
        res = []
        t = 0
        while t <= len(value_ls) -1 :
            if num >= value_ls[t]:
                res.append(symbol_ls[value_ls.index(value_ls[t])])
                num = num - value_ls[t]
                t = t - 1
            t = t + 1
        return "".join(res)


if __name__ == '__main__':
    sol = Solution()
    assert sol.intToRoman(1994) == "MCMXCIV"
    assert sol.intToRoman(3) == "III"
    assert sol.intToRoman(4) == "IV"
    assert sol.intToRoman(9) == "IX"
    assert sol.intToRoman(58) == "LVIII"
    assert sol.intToRoman(20) == "XX"
