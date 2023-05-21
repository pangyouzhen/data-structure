class Solution:
    def partitionString(self, s: str) -> int:
        pre_group = set()
        n = 0
        for i in s:
            if i not in pre_group:
                pre_group.add(i)
            else:
                print(pre_group)
                pre_group = set()
                n += 1
        return n


if __name__ == '__main__':
    func = Solution().partitionString
    s = "abacaba"
    print(func(s))