from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        res[0] = nums[0]
        for i in range(1, len(nums)):
            n = res[i - 1] + nums[i]
            res[i] = n
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    func = Solution().runningSum
    print(func(nums))
