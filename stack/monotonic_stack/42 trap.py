from typing import List


class Solution:
    # todo
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        ans = 0
        while left < right:
            # print(f"l is {l},r is {r},max_l is {max_l},max_r is {max_r}")
            if max_left < max_right:
                ans += max_left - height[left]
                left += 1
                max_left = max(max_left, height[left])
            else:
                ans += max_right - height[right]
                right -= 1
                max_right = max(max_right, height[right])
            print(f"{left},,{right},,{max_left},,{max_right}")
        return ans

    def trap2(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        ans = 0
        while left < right:
            # print(f"l is {l},r is {r},max_l is {max_l},max_r is {max_r}")
            if height[left] < height[right]:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    ans += max_left - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    ans += max_right - height[right]
                right -= 1
            print(f"{left},,{right},,{max_left},,{max_right},, {height[left]},,{height[right]}")
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(sol.trap2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
