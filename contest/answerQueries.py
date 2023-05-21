from typing import List
from bisect import bisect


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        m = [0] * len(nums)
        for i in range(len(nums)):
            m[i] = nums[i] + m[i - 1]
        print(m)
        a = [bisect(m, i) for i in queries]
        return a


if __name__ == '__main__':
    func = Solution().answerQueries
    nums = [4, 5, 2, 1]
    queries = [3, 10, 21]
    print(func(nums, queries))
