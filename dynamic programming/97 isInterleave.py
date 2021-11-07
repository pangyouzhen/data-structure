from pysnooper import snoop


class Solution:
    # @snoop()
    # todo
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        pass


if __name__ == '__main__':
    sol = Solution()
    # s1 = ""
    # s2 = ""
    # s3 = ""
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(sol.isInterleave(s1, s2, s3))
