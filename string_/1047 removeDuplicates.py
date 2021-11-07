class Solution:
    def removeDuplicates(self, S: str) -> str:
        #         栈的思想
        output = []
        for i in S:
            if output and i == output[-1]:
                output.pop()
            else:
                output.append(i)
        return "".join(output)


if __name__ == '__main__':
    S = "abbaca"
    S1 = "aaaaaaaaa"
    sol = Solution()
    print(sol.removeDuplicates(S))
    print(sol.removeDuplicates(S1))
