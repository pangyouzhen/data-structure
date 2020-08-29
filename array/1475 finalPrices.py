from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i, v in enumerate(prices[:-1]):
            for t, min_v in enumerate(prices[i + 1:]):
                if min_v <= v:
                    res.append(v - min_v)
                    break
                elif t == len(prices[i + 1:]) - 1:
                    res.append(v)
        res.append(prices[-1])
        return res


if __name__ == '__main__':
    prices = [8, 4, 6, 2, 3]
    sol = Solution()
    print(sol.finalPrices(prices))
