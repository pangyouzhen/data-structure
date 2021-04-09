class Solution:
    def calculate(self, s: str) -> int:
        symbol = ["+", "-"]
        a = 0
        res = [""]
        while a < len(s):
            v = s[a]
            if v.isdigit() and (res[-1] not in symbol):
                res[-1] += v
            elif v == "+" or v == "-":
                res.append(v)
            elif v == "*":
                last_number = res[-1]
                a += 1
                a, next_number = self.next_number_(a, s)
                curr_number = last_number * next_number
                res.append(curr_number)
            elif v == "/":
                last_number = res[-1]
                a += 1
                a, next_number = self.next_number_(a, s)
                curr_number = int(last_number / next_number)
                res.append(curr_number)
            a += 1
        print(res)
        return eval("".join(res))

    def next_number_(self, ind, s):
        next_number = []
        while ind < len(s) and s[ind].isdigit():
            next_number.append(s[ind])
            ind += 1
        next_number = int("".join(next_number))
        return ind, next_number


if __name__ == '__main__':
    sol = Solution()
    # print(sol.next_number_(2, "3+112+"))
    func = sol.calculate
    assert func("3+2*2") == 7
    assert func("3/2") == 1
    print(func("14/3*2"))
