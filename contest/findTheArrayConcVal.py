from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        end = len(nums) - 1
        start = 0
        res = 0
        while start < end:
            res += self.join_num(nums[start], nums[end])
            start += 1
            end -= 1
        if len(nums) % 2 != 0:
            res += nums[int(len(nums)/2)]
        return res

    def join_num(self, num1: int, num2: int):
        return int("".join([str(num1), str(num2)]))
