class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if cost1 > total and cost2 > total:
            return 1
        else:
            res = 0
            n = 0
            val = total
            while val >= 0:
                n += 1
                res += int(val / cost2) + 1
                val = total - n * cost1
            return res


if __name__ == "__main__":
    func = Solution().waysToBuyPensPencils
    total = 8
    cost1 = 5
    cost2 = 10
    print(func(total, cost1, cost2))
