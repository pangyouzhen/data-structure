class Solution:
    def isValid(self, s: str) -> bool:
        all_ = ["()", "[]", "{}"]
        a = []
        for i in s:
            a.append(i)
            if "".join(a[-2:]) in all_:
                del a[-2:]
        if a != []:
            return False
        return True


if __name__ == '__main__':
    nums = "(]"
    nums2 = "()"
    sol = Solution()
    print(sol.isValid(nums))
    print(sol.isValid(nums2))