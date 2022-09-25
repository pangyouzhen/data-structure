class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        a = {"2", "5", "6", "9"}
        b = {"3", "4", "7"}
        for i in range(1, n + 1):
            s = set(str(i))
            if s & a and not s & b:
                res += 1
        return res
