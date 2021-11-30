from collections import Counter
from pysnooper import snoop


class Solution:
    # @snoop()
    def nextBeautifulNumber(self, n: int) -> int:
        n += 1
        while True:
            if self.is_beautiful_number(n):
                return n
            else:
                n += 1

    def is_beautiful_number(self, n: int):
        res = True
        c = Counter(str(n))
        for i, v in c.items():
            if int(i) != int(v):
                res = False
                break
        return res


if __name__ == '__main__':
    func = Solution().nextBeautifulNumber
    print(func(1330))
