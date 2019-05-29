class Solution:
    # def twoSum(self, nums, target):
    # t = target / 2
    # print(t)
    # for i, v in enumerate(nums):
    #     if ((v == t) and (t in nums[i + 1:])):
    #         if (i != (nums[i + 1:].index(v) + i + 1)):
    #             return [i, nums[i + 1:].index(v) + i + 1]
    #     elif ((v != t) and ((target - v) in nums)):
    #         return [i, nums.index(target - v)]

    def twoSum(self, nums, target):
        for i, n in enumerate(nums):
            if ((target - n) in nums) and (nums.index(target - n) != i):
                print(nums.index(target - n))
                return sorted([i, nums.index(target - n)])


if __name__ == "__main__":
    solution = Solution()
    res = solution.twoSum([3,3], 6
                          )
    print(res)

# 1. 才开始没有使用enumerate 函数，得到索引,使用enumerate  函数，其实时使用了hash table
# 2. 考虑相同元素的情况时，考虑的不周全，list.index虽然只能得到第一个元素的位置，倒是时两个相同的元素，[1,2,1]，对于index为0判断时
# ，得到的index肯定是0，但是循环到第二个1时得到的时得到的index为第一个nums的index，两者的index不同，自己在两个相同元素时花费了较多时间
