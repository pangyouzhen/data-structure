from typing import List


# https://www.bilibili.com/video/av45844036?from=search&seid=4933796386934297862

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        # backtracking
        result = []
        nums = []

        def dfs(lst, nums, pos):
            print(f'lst is {lst},nums is {nums}, pos is {pos}')
            result.append(lst[:])
            for i in range(pos, len(nums)):
                lst.append(nums[i])
                dfs(lst, nums, i + 1)
                lst.pop()

        dfs(result, nums, 0)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(3))
