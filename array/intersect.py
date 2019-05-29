class Solution:
    def intersect(self, nums1, nums2):
        sort_num1 = sorted(nums1)
        sort_num2 = sorted(nums2)
        a = []
        for i, v in enumerate(sort_num1):
            if v in sort_num2:
                sort_num2.pop(sort_num2.index(v))
                a.append(v)
        return a


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    res = sol.intersect(nums1, nums2)
    print(res)
