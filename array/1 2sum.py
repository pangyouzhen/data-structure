class Solution:
    def twoSum(self, nums, target):
        # 1. 因为返回的是原先的索引，排序后的索引是不一样的, 所以构建另外一个需要zip记录原先的位置
        #  直接sort 会损失原先的位置信息
        ind = list(range(len(nums)))
        nums_zip = zip(nums, ind)
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
        # 双指针时间复杂度 O(n) 加上排序的时间复杂度


if __name__ == "__main__":
    solution = Solution()
    res = solution.twoSum([3, 2, 4], 6)
    print(res)
