import pysnooper


class Solution(object):
    @pysnooper.snoop()
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c = 0
        for i, v in enumerate(nums[1:]):
            if v - nums[i] <= 0:
                c += 1
                if i - 1 >= 0 and v - nums[i - 1] > 0:
                    continue
                elif i - 1 == -1:
                    continue
                else:
                    return False
        return True


if __name__ == '__main__':
    # a = [10, 1, 2, 5, 7]
    a = [105, 924, 32, 968]
    sol = Solution()
    print(sol.canBeIncreasing(a))
