class Solution:
    def romanToInt(self, s):
        roman_dict = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        right = 0
        k = ''
        res = 0
        keys = roman_dict.keys()
        while right < len(s):
            print(k)
            k += s[right]
            right += 1
            if len(k) == 2 and k in keys:
                res += roman_dict[k]
                k = ''
            elif len(k) == 2 and k not in keys:
                res += roman_dict[k[0]]
                k = k[1:]
            if len(k) == 1 and right == len(s):
                res += roman_dict[k]
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.romanToInt("III") == 3
    print(sol.romanToInt("MCMXCIV"))
    # print(sol.romanToInt("III"))
    # print(sol.romanToInt("MCMXCIV") == 1994)
    # print(sol.romanToInt("III") == 3)
