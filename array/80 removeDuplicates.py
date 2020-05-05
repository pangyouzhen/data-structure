from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        t = {}
        k = 0
        # 对于原地删除元素的不能用for循环，否则会造成index的错误
        while k < len(nums):
            i = nums[k]
            str_i = str(i)
            if str_i not in t.keys():
                t[str_i] = 1
            else:
                t[str_i] = t[str_i] + 1
            if t[str_i] > 2:
                del nums[k]
                t[str_i] = 2
                k = k - 1
            k = k + 1
        return len(nums)


if __name__ == '__main__':
    # nums = [1, 1, 2, 3, 3, 3]
    sol = Solution()
    # print(sol.removeDuplicates(nums))
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(sol.removeDuplicates(nums2))
