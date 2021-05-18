class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def is_vowels(ch):
            return int(ch in "aeiou")

        n = len(s)
        t = sum(1 for i in range(k) if is_vowels(s[i]))
        ans = t
        for i in range(k, n):
            t += is_vowels(s[i]) - is_vowels(s[i - k])
            ans = max(ans, t)
        return ans


if __name__ == '__main__':
    s = "abciiidef"
    k = 3
    sol = Solution()
    print(sol.maxVowels(s, k))
