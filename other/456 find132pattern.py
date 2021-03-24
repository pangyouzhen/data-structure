from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)
        numsi = nums[0]
        for j in range(N):
            for k in range(N - 1, j, -1):
                if numsi < nums[k] and nums[k] < nums[j]:
                    return True
            numsi = min(numsi, nums[j])
        return False


if __name__ == '__main__':
    # nums = [1, 2, 3, 4]
    nums = [3, 1, 4, 2]
    sol = Solution()
    print(sol.find132pattern(nums))
