# 匹配的问题一般用stack
class Solution:
    def isValid(self, s):
        stack = []
        open = ["(", "{", "["]
        lookup = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in open:
                stack.append(i)
            #           [{]} ////[{[
            elif i in lookup:
                if len(stack) == 0:
                    return False
                elif lookup[i] != stack[-1] or lookup[i] not in stack:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0


if __name__ == '__main__':
    sol = Solution().isValid
    assert sol("()[]{}") == True
    assert sol("(]") == False
    assert sol("([)]") == False
    assert sol("{[]}") == True
    assert sol("((") == False
