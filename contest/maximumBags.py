from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        minus_cap = [i - v for i, v in zip(capacity, rocks)]
        minus_cap.sort()
        res = 0
        for i, v in enumerate(minus_cap):
            if additionalRocks >= v:
                res += 1
                additionalRocks -= v
        return res


if __name__ == "__main__":
    func = Solution().maximumBags
    nums = []
    print(func(nums))
