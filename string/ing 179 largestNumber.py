from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(i) for i in nums]
        l = len(nums_str)
        res = []
        t = 0
        while t < l:
            first_nums = [int(i[0]) for i in nums_str]
            max_first = max(first_nums)
            first_index = [i for i, v in enumerate(first_nums) if int(v) == max_first]
            if len(first_index) == 1:
                res.append(str(nums_str[first_index[0]]))
                nums_str.pop(first_index[0])
            else:
                first_ls = max([int(nums_str[i]) for i in first_index])
                res.append(str(first_ls))
                nums_str.pop(nums_str.index(str(first_ls)))
            t = t + 1
        return "".join(res)


if __name__ == '__main__':
    sol = Solution()
    assert sol.largestNumber([10, 2]) == "210"
    print(sol.largestNumber([3, 30, 34, 5, 9]))
    # assert sol.largestNumber([3, 30, 34, 5, 9]) == "9534330"
