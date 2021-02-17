from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        total_nums = len(nums) * len(nums[0])
        if total_nums != (r * c):
            return nums
        else:
            nums_ = [j for i in nums for j in i]
            res = [nums_[i * c:(i + 1) * c] for i in range(0, r)]
            return res


if __name__ == '__main__':
    nums = [[1, 2], [3, 4]]
    sol = Solution()
    print(sol.matrixReshape(nums, 2, 2))
