from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 1
        min_val = min(nums)
        max_val = max(nums)
        min_ind = nums.index(min_val)
        max_ind = nums.index(max_val)
        min_ = min(min_ind, max_ind)
        max_ = max(min_ind, max_ind)
        left = max_ + 1
        right = l - min_
        left_right = min_ + 1 + (l - max_)
        return min(left, right, left_right)


if __name__ == '__main__':
    func = Solution().minimumDeletions
    nums = [2, 10, 7, 5, 4, 1, 8, 6]
    print(func(nums))
