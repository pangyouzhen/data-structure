class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """


        nums1 = nums1.map(lambda x: nums1.pop(x))

        i = j = k = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                pass


if __name__ == '__main__':
    n1 = [1, 2, 3, 0, 0, 0]
    m = 3
    n2 = [2, 5, 6]
    n = 3

    sol = Solution()
    assert sol.merge(n1, m, n2, n) == [1, 2, 2, 3, 5, 6]
