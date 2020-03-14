from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        # backtracking
        def dfs(lst, nums, pos):
            print(f'lst is {lst},nums is {nums}, pos is {pos}')
            res1 = lst[:]
            res1.sort()
            if res1 not in result:
                result.append(res1)
            for i in range(pos, len(nums)):
                lst.append(nums[i])
                dfs(lst, nums, i + 1)
                lst.pop()

        dfs([], nums, 0)
        return result


if __name__ == '__main__':
    subsets = [1, 2, 2]
    sol = Solution()
    print(sol.subsetsWithDup(subsets))
