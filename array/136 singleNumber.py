from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t = Counter(nums)
        return t.most_common()[-1][0]



if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([1, 2, 4, 1, 2]))

