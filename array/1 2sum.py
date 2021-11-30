class Solution:
    def twoSum(self, nums, target):
        #  直接sort会损失原先的位置信息
        nums_zip = [(v, i) for i, v in enumerate(nums)]
        numbers = sorted(nums_zip)
        start = 0
        end = len(nums) - 1
        while start < end:
            sum_ = numbers[start][0] + numbers[end][0]
            if sum_ == target:
                return [numbers[start][1], numbers[end][1]]
            elif sum_ > target:
                end -= 1
            else:
                start += 1


if __name__ == "__main__":
    solution = Solution()
    res = solution.twoSum([3, 2, 4], 6)
    print(res)
