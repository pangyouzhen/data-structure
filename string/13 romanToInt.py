class Solution:
    def romanToInt(self, s):
        roman_ = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        t = 0
        res = 0
        while t < len(s):
            try:
                if roman_[s[t]] >= roman_[s[t + 1]]:
                    # print(roman_[s[t]])
                    res += roman_[s[t]]
                    t += 1
                else:
                    # print(roman_[s[t - 1]])
                    res += roman_[s[t + 1]]  - roman_[s[t]]
                    t = t + 2
            except IndexError as e:
                res += roman_[s[t]]
                break
        return res


# problem：切分之后，匹配之后如何跳过这个索引,跳过这个索引用while
# while  即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务。其基本形式为, for 是对所有的进行循环
if __name__ == '__main__':
    sol = Solution()
    # assert sol.romanToInt("III") == 3
    print(sol.romanToInt("MCMXCIV"))
    print(sol.romanToInt("III"))
    # print(sol.romanToInt("MCMXCIV") == 1994)
    # print(sol.romanToInt("III") == 3)
