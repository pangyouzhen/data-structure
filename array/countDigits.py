class Solution:
    def countDigits(self, num: int) -> int:
        s = str(num)
        n = 0
        for i in s:
            if num % int(i) == 0:
                n += 1
        return n 