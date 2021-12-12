from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        l = len(nums)
        for i in range(l + 1):
            for j in range(i + 1, l + 1):
                n = nums[i:j]
                max_val = max(n)
                min_val = min(n)
                res += (max_val - min_val)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    func = Solution().subArrayRanges
    print(func(nums))
