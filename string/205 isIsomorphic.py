class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # 问题在于两者需要同时进行匹配，第一个e配上了a，那么s需要判断第二个letter，t也需要，用zip函数，不能用笛卡尔乘机，
        if s == "":
            return True
        return [s.index(i) for i in s] == [t.index(i) for i in t]


if __name__ == '__main__':
    sol = Solution()
    # assert sol.isIsomorphic("egg", "add") == True
    # assert sol.isIsomorphic("foo", "bar") == False
    # assert sol.isIsomorphic("paper", "title") == True
    assert sol.isIsomorphic("ab", "aa") == False
