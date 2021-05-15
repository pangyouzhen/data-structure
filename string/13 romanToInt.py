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
        a = []
        t = 0
        while t < len(s):
            if t + 1 < len(s) and roman_[s[t]] < roman_[s[t + 1]]:
                a.append(s[t:t + 2])
                t = t + 1
            else:
                a.append(s[t])
            t = t + 1
        ls = list(map(lambda x: roman_[x], a))
        return sum(ls)


# problem：切分之后，匹配之后如何跳过这个索引,跳过这个索引用while
# while  即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务。其基本形式为, for 是对所有的进行循环
if __name__ == '__main__':
    sol = Solution()
    # assert sol.romanToInt("III") == 3
    assert sol.romanToInt("MCMXCIV") == 1994
    assert sol.romanToInt("III") == 3
