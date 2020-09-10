from typing import List


class Solution:
    def combinationSum(self, candidates, target: int):
        global res
        res = []
        one_ans = []
        start = 0
        candidates.sort()
        print(candidates)
        self.combinationSum_memo(candidates, target, start, one_ans)
        return res

    def combinationSum_memo(self, candidates, target, start, one_ans):
        if target == 0:
            res.append(one_ans[:])
            return
        for i in range(start, len(candidates)):
            print(f'{(start + 1) * "+"},for {i=} in range({start=},{len(candidates)=}), {target = },{one_ans = }')
            if candidates[i] > target: return
            one_ans.append(candidates[i])
            self.combinationSum_memo(candidates, target - candidates[i], i, one_ans)
            one_ans.pop()
        return


# 下面的错误错误在那里，如何形象的解决这个问题，怎样和树形结构结合起来
# class Solution:
#     def combinationSum(self, candidates, target: int):
#         global res
#         res = []
#         one_ans = []
#         start = 0
#         self.combinationSum_memo(candidates, target, start, one_ans)
#         return res
#
#     def combinationSum_memo(self, candidates, target, start, one_ans):
#         if target < 0:
#             return
#         elif target == 0:
#             one_ans.sort()
#             if one_ans not in res:
#                 res.append(one_ans[:])
#             return
#         for i in candidates:
#             print(f'{i=},{target - i=},{one_ans=}')
#             one_ans.append(i)
#             self.combinationSum_memo(candidates, target - i, start, one_ans)
#             one_ans.pop()
#         return

if __name__ == '__main__':
    sol2 = Solution()
    print(sol2.combinationSum([2, 3, 6, 7], 7))
    print(sol2.combinationSum([2, 3, 5], 8))
    print(sol2.combinationSum([8, 7, 4, 3], 11))
