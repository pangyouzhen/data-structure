class Solution:
    def isPowerOfFour(self, n):
        while 1:
            if n == 1:
                return True
            if n / 4 == 1:
                return True
            elif int(n / 4) < 1:
                return False
            else:
                n = n / 4
