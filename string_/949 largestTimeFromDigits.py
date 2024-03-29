from typing import List


class Solution:
    def __init__(self):
        self.all_ans = []

    def largestTimeFromDigits(self, arr: List[int]) -> str:
        pass

    def dfs(self, arr, one_ans, start):
        if len(one_ans) == 4:
            self.all_ans.append(one_ans[:])
            return
        for i in arr[start:]:
            one_ans.append(i)
            self.dfs(arr, one_ans, start + 1)
            one_ans.pop()


if __name__ == '__main__':
    sol = Solution()
    # func = Solution().largestTimeFromDigits
    # func2 = Solution().dfs
    arr = [1, 2, 3, 4]
    one_ans = []
    start = 0
    print(sol.dfs(arr, one_ans, start))
    print(sol.all_ans)
