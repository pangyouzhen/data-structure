from itertools import combinations
from typing import List

# TODO
# 这不是回溯，这是0-1背包问题
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k == 0:
            return self.dfs(s / k, s, nums)
        return False

    def dfs(self, k, s, nums):
        if s < k or s % k != 0 or max(nums) > k:
            return False
        for i in range(len(nums)):
            print("****************************")
            print(nums)
            print(i)
            for j in combinations(nums, i):
                if sum(j) == k:
                    print("------------------------")
                    print(nums)
                    print(j)
                    s -= k
                    for t in j:
                        nums.remove(t)
                    self.dfs(k, s, nums)
        return True


if __name__ == "__main__":
    func = Solution().canPartitionKSubsets
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print(func(nums, k))
