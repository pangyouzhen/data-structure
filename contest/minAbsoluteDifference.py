from typing import List
from sortedcontainers import SortedList


class Solution:

    def minAbsoluteDifference(self, nums: List[int], k: int) -> int:
        ans = float("inf")
        sl = SortedList([float("-inf"), float("inf")])  # 哨兵
        for x, y in zip(nums, nums[k:]):
            print(x)
            print(y)
            sl.add(x)
            print(sl)
            j = sl.bisect_left(y)
            ans = min(ans, sl[j] - y, y - sl[j - 1])
        return ans
if __name__ == "__main__":
    func = Solution().minAbsoluteDifference
    nums = [1,2,3,4]
    x = 3
    print(func(nums,x))
            