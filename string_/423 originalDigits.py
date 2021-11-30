from collections import defaultdict,Counter


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
        c = Counter(s)

        cnt = [0] * 10
        cnt[0] = c["z"]
        cnt[2] = c["w"]
        cnt[4] = c["u"]
        cnt[6] = c["x"]
        cnt[8] = c["g"]

        cnt[3] = c["h"] - cnt[8]
        cnt[5] = c["f"] - cnt[4]
        cnt[7] = c["s"] - cnt[6]

        cnt[1] = c["o"] - cnt[0] - cnt[2] - cnt[4]

        cnt[9] = c["i"] - cnt[5] - cnt[6] - cnt[8]

        return "".join(str(x) * cnt[x] for x in range(10))



if __name__ == '__main__':
    func = Solution().originalDigits
    s = "zerozero"
    print(func(s))
