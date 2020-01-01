from typing import List


# 双指针问题是从两边开始计算吗？，这个是个双指针问题

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            water = min(height[left], height[right]) * (right - left)
            if water > res:
                res = water

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(sol.maxArea([1, 8]))
