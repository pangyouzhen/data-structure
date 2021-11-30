from typing import List
from pysnooper import snoop


class Solution:
    # @snoop()
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pre_ind = None
        for i, v in enumerate(nums):
            if v == 1:
                # if condition is not None 和 if True是不一样的
                # pre_ind 起始是None，如果赋值为0的话就是False，所以这里不用if pre_ind,
                # 这里只要满足is not None 就行了
                if pre_ind is not None and (i - pre_ind - 1 < k):
                    return False
                pre_ind = i
        return True


if __name__ == '__main__':
    func = Solution().kLengthApart
    assert func([1, 0, 0, 0, 1, 0, 0, 1], 2) is True
    assert func([1, 0, 0, 1, 0, 1], 2) is False
    assert func([0, 1, 0, 1], 1) is True
    assert func([1, 0, 1], 2) is False
