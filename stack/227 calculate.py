class Solution:
    # 栈
    def calculate(self, s: str) -> int:
        s = s.replace("/", "//")
        return int(eval(s))

    # todo
    def calculate_stack(self, s: str) -> int:
        stack = []
        for i in s:
            stack.append(i)


if __name__ == '__main__':
    sol = Solution()
    func = sol.calculate
    assert func("3+2*2") == 7
    assert func("3/2") == 1
    print(func("14/3*2"))
