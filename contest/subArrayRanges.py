from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        l = len(nums)
        for i in range(l):
            mi = nums[i]
            ma = nums[i]
            for j in range(i, l):
                mi = min(mi, nums[j])
                ma = max(ma, nums[j])
                res += (ma - mi)  # 更新差值

        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    func = Solution().subArrayRanges
    print(func(nums))
