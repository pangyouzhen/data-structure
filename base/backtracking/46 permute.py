from typing import List



class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        one_ans = []
        self.permute_rec_memo(nums, one_ans)
        return self.res

    # 这里最终返回的是-> List[str]，所以每一个元素应该是str,所以one_ans应该是List[str]
    def permute_rec_memo(self, nums: List[int], one_ans: List[int]):
        # 递归的终止条件
        if len(one_ans) == len(nums):
            # 这里为什么用的是one_ans[:],如果用self.res.append(one_ans)增加的是一个对象，下一步递归又把元素pop了
            # id(one_ans[:]) 和 id(one_ans) 是不同的，相当于新添加了个对象
            self.res.append(one_ans[:])
            print("---------------------")
            return
        # 横向循环。确保只循环一次
        for i in range(len(nums)):
            print(f"for i in range({len(nums)}):")
            # 排除不合法的选择
            if nums[i] in one_ans:
                continue
            one_ans.append(nums[i])
            self.permute_rec_memo(nums, one_ans)
            one_ans.pop()
        return


if __name__ == '__main__':
    sol = Solution()
    b = sol.permute([1, 2, 3])
    print(b)
