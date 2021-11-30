from pysnooper import snoop
class Solution:
    # @snoop()
    def areNumbersAscending(self, s: str) -> bool:
        t = s.split()
        res = True
        last = -1
        for i in t:
            if i.isdigit():
                # print(i)
                if int(i) > last:
                    last = int(i)
                else:
                    res = False
        return res

if __name__ == '__main__':
    s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
    func = Solution().areNumbersAscending
    print(func(s))
