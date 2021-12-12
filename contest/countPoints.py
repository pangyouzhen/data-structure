from collections import defaultdict


class Solution:
    def countPoints(self, rings: str) -> int:
        l = len(rings)
        d = defaultdict(list)
        for i in range(1, l, 2):
            d[rings[i]].append(rings[i - 1])
        res = 0
        for k, v in d.items():
            v = "".join(v)
            if set(v) == set("RGB"):
                res += 1
        return res


if __name__ == '__main__':
    rings = "B0B6G0R6R0R6G9"
    sol = Solution().countPoints
    print(sol(rings))
