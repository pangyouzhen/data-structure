from typing import List


class Solution:
    #  todo
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # 超时
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if i != j:
        #             if abs(nums[i] - nums[j]) <= t and abs(i - j) <= k:
        #                 return True
        # return False
        pass

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    t = 0
    print(sol.containsNearbyAlmostDuplicate(nums, k=3, t=0))
