# combination
from typing import Iterable, List
from itertools import chain, combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_ans = []
        one_ans = []
        def dfs(nums,ind,one_ans):
            all_ans.append(one_ans[:])
            for i in range(ind,len(nums)):
                one_ans.append(nums[i])
                dfs(nums,i+1,one_ans)
                one_ans.pop()
        dfs(nums,0,one_ans)
        return all_ans        

    # python 没有内置的subset计算，但是可以从下面函数中得到
    def powerset(self, iterable: Iterable):
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    print(sol.subsets(nums))
    print([i for i in sol.powerset(nums)])
