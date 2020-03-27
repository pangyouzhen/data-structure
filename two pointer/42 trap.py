from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        l = 0
        r = len(height) - 1
        max_l = height[l]
        max_r = height[r]
        ans = 0
        while l < r:
            # print(f"l is {l},r is {r},max_l is {max_l},max_r is {max_r}")
            if max_l < max_r:
                print(f"{max_l - height[l]}")
                ans += max_l - height[l]
                l += 1
                max_l = max(max_l, height[l])
            else:
                ans += max_r - height[r]
                r -= 1
                max_r = max(max_r, height[r])
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
