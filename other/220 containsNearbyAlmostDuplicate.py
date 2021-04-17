from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # todo 滑动窗口 timeout
        n = len(nums)
        window = []
        for i in range(n):
            value = nums[i]
            for w in window:
                if abs(w - value) <= t:
                    return True
            window.append(value)
            if len(window) > k:
                del window[0]
        return False


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    t = 0
    print(sol.containsNearbyAlmostDuplicate(nums, k=3, t=0))
