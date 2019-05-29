class Solution:
    def romanToInt(self, s):
        roman_ = {
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
        a = []
        i = 0
        while (i < len(s)):
            if (s[i] == "I" or s[i] == "X" or s[i] == "C") and (s[i:i + 2] in roman_.keys()):
                value = roman_.get("%s" % s[i:i + 2])
                i = i + 2
            else:
                value = roman_.get("%s" % s[i])
                i = i + 1
            a.append(value)
        return a


# problem：切分之后，匹配之后如何跳过这个索引,跳过这个索引用while
# while  即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务。其基本形式为, for 是对所有的进行循环
if __name__ == '__main__':
    sol = Solution()
    res = sol.romanToInt("MCMXCIV")
    print(res)
    print(sum(res))
