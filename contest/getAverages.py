from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        l = len(nums)
        if (k * 2 + 1) > l:
            return [-1] * l
        res = [-(2 * k + 1)] * k
        t = sum(nums[0:(2 * k + 1)])
        res.append(t)
        for i in range(k + 1, l - k):
            m = res[-1] + nums[i + k] - nums[i - k - 1]
            res.append(m)
        last = [-(2 * k + 1)] * k
        res.extend(last)
        return [int(i / (2 * k + 1)) for i in res]


if __name__ == '__main__':
    nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
    k = 3
    func = Solution().getAverages
    print(func(nums, k))
