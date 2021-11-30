from typing import List


class Solution:
    def permuteUnique(self, nums):
        curr = []
        ans = []

        def dfs(nums: List[int], d: int, n: int, used: List[bool], curr: List[int], ans: List[List[int]]):
            if d == n and curr[:] not in ans:
                ans.append(curr[:])
                return
            for i in range(0, len(nums)):
                if used[i]:
                    continue
                used[i] = True
                curr.append(nums[i])
                dfs(nums, d + 1, n, used, curr, ans)
                curr.pop()
                used[i] = False

        dfs(nums, 0, len(nums), [False] * len(nums), curr, ans)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.permuteUnique([1, 1, 2]))
