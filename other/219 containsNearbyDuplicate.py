from typing import List


class Solution:
    # TODO 滑动窗口
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a = {}
        for i, v in enumerate(nums):
            if v not in a:
                a[v] = [i]
            else:
                a[v].append(i)
        print(a)
        for key, val in a.items():
            if len(val) > 1:
                t = min([val[i] - val[i - 1] for i in range(1, len(val))])
                if t <= k:
                    return True
        return False


if __name__ == '__main__':
    nums = [1, 0, 1, 1]
    k = 1
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))
