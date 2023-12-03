class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high+1):
            if self.sym(i):
                res += 1
                print(i)
        return res

    def sym(self, num: int):
        s = str(num)
        l = len(s)
        if l % 2 == 0:
            t1 = map(int, s[:int(l/2)])
            t2 = map(int, s[int(l/2):])
            if sum(t1) == sum(t2):
                return True
        return False
