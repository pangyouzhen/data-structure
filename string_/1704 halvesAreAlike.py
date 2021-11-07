class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        median = int(n / 2)
        a = s[:median]
        b = s[median:]
        vocab = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        def vocab_count(t: str):
            c = 0
            for i in t:
                if i in vocab:
                    c += 1
            return c

        return vocab_count(a) == vocab_count(b)


if __name__ == '__main__':
    sol = Solution()
    print(sol.halvesAreAlike("book"))
