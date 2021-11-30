class Solution:
    def secondHighest(self, s: str) -> int:
        res = list(set([int(i) for i in s if i.isdigit()]))
        res.sort()
        if len(res) > 1:
            return res[-2]
        return -1


if __name__ == '__main__':
    s = "dfa12321afd"
    sol = Solution()
    print(sol.secondHighest(s))
