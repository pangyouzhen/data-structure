from typing import List
from bisect import bisect_left


class Solution:
    def avoidFlood(self, nums: List) -> List:
        n = len(nums)
        ans = [-1] * n
        last_rain = {}
        suns = []
        for i, v in enumerate(nums):
            if v == 0:
                suns.append(i)
                ans[i] = 1
            else:
                if v in last_rain:
                    it = bisect_left(suns, last_rain[v]) - 1
                last_rain[v] = i
        return ans


if __name__ == '__main__':
    nums = [0, 1, 2, 0, 2, 1]
    sol = Solution()
    # nums2 = [1, 2, 0, 0, 2, 1]
    # nums2 = [1, 0, 2, 3, 0, 1, 2]
    # print(sol.avoidFlood(nums))
    # print(sol.avoidFlood(nums2))
    nums3 = [1, 0, 2, 0, 2, 1]
    print(sol.avoidFlood(nums3))
