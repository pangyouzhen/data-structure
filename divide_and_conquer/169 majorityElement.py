from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElement([3, 2, 3]))
