class Solution:
    def isPalindrome(self, x):
        a = []
        if x < 0:
            return False
        else:
            while (x > 0):
                remainder = x % 10
                x = x // 10
                a.append(remainder)
        if a == a[::-1]:
            return True
        else:
            return False


# 既然不能转化为String，1234那么千位上为1，百位上为2 这样切分一下
# 那么就需要取整和取余的操作
#
# 123 / 10 = 12...3
# 那么个位数就有了
#
# 12 / 10 = 1...2
# 那么百位数就有了
#
# 1 / 10 = 0...1
# 那么千位数就有了
if __name__ == '__main__':
    sol = Solution()
    res = sol.isPalindrome(-121)
    print(res)
