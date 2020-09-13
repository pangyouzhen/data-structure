class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = 0
        right = len(A) -1
        res = 0

        while left < right:
            s