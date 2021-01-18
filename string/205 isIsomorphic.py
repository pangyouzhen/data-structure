class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 问题在于两者需要同时进行匹配，第一个e配上了a，那么s需要判断第二个letter，t也需要，用zip函数，不能用笛卡尔乘机，
        omoraphic_dict = {}
        for i in range(len(s)):
            if s[i] not in omoraphic_dict.keys():
                omoraphic_dict[s[i]] = t[i]
                s = s.replace(s[i], t[i])
        if s == t:
            return True
        return False


if __name__ == '__main__':
    sol = Solution()
    # assert sol.isIsomorphic("egg", "add") == True
    # assert sol.isIsomorphic("foo", "bar") == False
    # assert sol.isIsomorphic("paper", "title") == True
    assert sol.isIsomorphic("ab", "aa") == False
