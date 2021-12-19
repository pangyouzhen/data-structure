class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            remainder = numBottles % numExchange
            divisor = numBottles // numExchange
            numBottles = remainder + divisor
            res += divisor
        return res


if __name__ == '__main__':
    func = Solution().numWaterBottles
    numBottles = 15
    numExchange = 4
    print(func(numBottles, numExchange))
