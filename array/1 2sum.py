class Solution:
    def twoSum(self, nums, target):
        for i, n in enumerate(nums):
            if ((target - n) in nums) and (nums.index(target - n) != i):
                print(nums.index(target - n))
                return sorted([i, nums.index(target - n)])

    def two_sum_two_pointers(self, nums, target):
        # nums.sort()
        nums1 = sorted(nums)
        # 错误的，主要点在下面
        # 1. 因为返回的是原先的索引，排序后的索引是不一样的,
        # 2. 另外重复项的问题如何解决，单纯的nums.index 是解决不了的
        i, j = 0, len(nums1) - 1
        while i < j:
            sum = nums1[i] + nums1[j]
            if sum < target:
                i = i + 1
            elif sum > target:
                j = j - 1
            else:
                return [nums.index(nums1[i]), nums.index(nums1[j])]
        return None


if __name__ == "__main__":
    solution = Solution()
    res = solution.two_sum_two_pointers([3, 2, 4], 6)
    print(res)

# 1. 才开始没有使用enumerate 函数，得到索引,使用enumerate  函数，其实时使用了hash table
# 2. 考虑相同元素的情况时，考虑的不周全，list.index虽然只能得到第一个元素的位置，倒是时两个相同的元素，[1,2,1]，对于index为0判断时
# ，得到的index肯定是0，但是循环到第二个1时得到的时得到的index为第一个nums的index，两者的index不同，自己在两个相同元素时花费了较多时间
# sort is important
