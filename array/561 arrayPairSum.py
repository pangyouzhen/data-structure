from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(0, len(nums), 2):
            res += min(nums[i:i + 2])
        return res


if __name__ == '__main__':
    nums = [1, 4, 3, 2]
    sol = Solution()
    print(sol.arrayPairSum(nums))
