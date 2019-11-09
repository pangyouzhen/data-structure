class Solution:
    def reverse(self, x):
        if x >= 0:
            reversed_value = int(''.join([i for i in reversed(str(x))]))
            if reversed_value > 2 ** (31) - 1:
                return 0
            else:
                return reversed_value
        else:
            reversed_value = -(int(''.join([i for i in reversed(str(abs(x)))])))
            if reversed_value < -2 ** (31):
                return 0
            else:
                return reversed_value


if __name__ == '__main__':
    sol = Solution()
    res = sol.reverse(1534236469)
    print(res)
