from collections import defaultdict


# todo
class Solution:
    # 暴力解法-超时
    def originalDigits_(self, s: str) -> str:
        a = {"zero": "0",
             "one": "1",
             "two": "2",
             "three": "3",
             "four": "4",
             "five": "5",
             "six": "6",
             "seven": "7",
             "eight": "8",
             "nine": "9"}
        m = list(s)
        res = []
        while m:
            for i in a.keys():
                if set(i) <= set(m):
                    res.append(int(a[i]))
                    for j in i:
                        m.remove(j)
        res.sort()
        res = [str(i) for i in res]
        return "".join(res)

    def originalDigits(self, s: str) -> str:
        d = defaultdict(list)
        a = {"zero": "0",
             "one": "1",
             "two": "2",
             "three": "3",
             "four": "4",
             "five": "5",
             "six": "6",
             "seven": "7",
             "eight": "8",
             "nine": "9"}

        k = set("".join(a.keys()))
        for i in k:
            for j in a.keys():
                if i in j:
                    d[i].append(a[j])


if __name__ == '__main__':
    func = Solution().originalDigits
    s = "zerozero"
    print(func(s))
