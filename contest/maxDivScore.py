from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divisors = list(set(divisors))
        max_score = 0
        ind = 0
        for i,v in enumerate(divisors):
            score = 0
            for j in nums:
                if j % v == 0:
                    score += 1
            if score > max_score:
                max_score = score
                ind = v
            elif score == max_score:
                ind = min(ind,v)
        if max_score == 0:
            return min(divisors)
        return ind