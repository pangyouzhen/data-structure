class Solution:
    def removeDuplicates(self, S: str) -> str:
        S_lst = list(S)
        t = 1
        while t < len(S_lst):
            if t < 1:
                t = 1
            if S_lst[t] == S_lst[t - 1]:
                del S_lst[t - 1]
                del S_lst[t - 1]
                t -= 2
            t += 1
        return "".join(S_lst)


if __name__ == '__main__':
    S = "abbaca"
    S1 = "aaaaaaaa"
    sol = Solution()
    print(sol.removeDuplicates(S))
    print(sol.removeDuplicates(S1))
