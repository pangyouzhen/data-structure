class Solution:

    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', "e", 'i', 'o', 'u'}
        ans, n = 0, len(word)
        # print(n)
        for i in range(n - 4):
            for j in range(i, n + 1):
                # print(i, j)
                # print(word[i:j])
                if set(word[i:j]) == vowels:
                    ans += 1
        return ans


if __name__ == '__main__':
    func = Solution().countVowelSubstrings
    print(func("uaieuoua"))
