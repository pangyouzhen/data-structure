class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0
        while k:
            if numOnes > 0:
                numOnes -= 1
                res += 1
            elif numZeros > 0:
                numZeros -= 1
            elif numNegOnes > 0:
                res -= 1
            k -= 1
        return res