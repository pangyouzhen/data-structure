from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element, num = Counter(nums).most_common()[0]
        if num > (len(nums) / 2):
            return element
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElement([3, 2, 3]))
