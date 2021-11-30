class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        special_roman = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        res = 0
        for i in special_roman.keys():
            if i in s:
                res += special_roman[i]
                s = s.replace(i, "")
        if s:
            for j in s:
                res += roman[j]
        return res

# if __name__ == '__main__':
#     func = Solution().romanToInt
