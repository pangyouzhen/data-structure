from typing import List


# combination


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        # backtracking
        def dfs(lst, nums, pos):
            print(f'lst is {lst},nums is {nums}, pos is {pos}')
            result.append(lst[:])
            for i in range(pos, len(nums)):
                lst.append(nums[i])
                dfs(lst, nums, i + 1)
                lst.pop()

        dfs([], nums, 0)
        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    print(sol.subsets(nums))
