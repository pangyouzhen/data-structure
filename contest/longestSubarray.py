from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        res, n = 0, 0
        for i in nums:
            if i == m:
                n += 1
                res = max(n, res)
            else:
                n = 0
        return res


if __name__ == '__main__':
    func = Solution().longestSubarray
    # nums = [1, 2, 3, 3, 2, 2]
    nums = [311155, 311155, 311155, 311155, 311155, 311155, 311155, 311155, 201191, 311155]
    print(func(nums))
