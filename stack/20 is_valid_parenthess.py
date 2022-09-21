class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            stack.append(i)
            last_two = "".join(stack[-2:])
            while last_two in ["()", "[]", "{}"]:
                stack.pop()
                stack.pop()
                last_two = "".join(stack[-2:])
        if stack:
            return False
        return True


if __name__ == '__main__':
    # nums = "(]"
    nums2 = "()"
    sol = Solution()
    # print(sol.isValid(nums))
    print(sol.isValid(nums2))
