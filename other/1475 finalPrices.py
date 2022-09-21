from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i, v in enumerate(prices):
            price = v
            for j in prices[i + 1:]:
                if v >= j:
                    price = v - j
                    break
            res.append(price)
        return res


if __name__ == '__main__':
    func = Solution().finalPrices
    prices = [8, 4, 6, 2, 3]
    print(func(prices))

