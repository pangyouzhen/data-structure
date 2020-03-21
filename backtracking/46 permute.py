class Solution:
    def permute(self, nums):
        curr = []
        ans = []

        def dfs(nums, d, n, used, one_ans, all_ans):
            if d == n:
                all_ans.append(one_ans[:])
                return
            for i in range(0, len(nums)):
                if used[i]:
                    continue
                used[i] = True
                one_ans.append(nums[i])
                dfs(nums, d + 1, n, used, one_ans, all_ans)
                one_ans.pop()
                used[i] = False

        dfs(nums, 0, len(nums), [False] * len(nums), curr, ans)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([1, 2, 3]))
