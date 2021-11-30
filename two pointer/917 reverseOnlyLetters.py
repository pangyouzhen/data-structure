class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        i = 0
        j = len(S) - 1
        S = list(S)
        while i < j:
            if (S[i].isalpha() and S[j].isalpha()):
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
            else:
                if not S[i].isalpha():
                    i += 1
                if not S[j].isalpha():
                    j -= 1
        return "".join(S)


if __name__ == '__main__':
    sol = Solution()
    assert sol.reverseOnlyLetters("ab-cd") == "dc-ba"
    assert sol.reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
    assert sol.reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
