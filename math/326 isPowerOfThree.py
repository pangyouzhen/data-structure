class Solution:
    def isPowerOfThree(self, n):
        while 1:
            if n ==1:
                return True
            if n / 3 == 1:
                return True
            elif int(n / 3) < 1:
                return False
            else:
                n = n / 3


if __name__ == '__main__':
    sol = Solution()
    assert sol.isPowerOfThree(27) == True
    assert sol.isPowerOfThree(28) == False
    assert sol.isPowerOfThree(243) == True
    assert sol.isPowerOfThree(45) == False
    assert sol.isPowerOfThree(1) == True
