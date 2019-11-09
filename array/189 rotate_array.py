from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, k):
            nums.insert(0, nums[-1])
            nums.pop(-1)


if __name__ == '__main__':
    sol = Solution()
    sol.rotate([1, 2, 3, 4, 5, 6, 7], 3)
