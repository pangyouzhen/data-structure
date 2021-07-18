class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        words = text.split(" ")
        c = 0
        for word in words:
            for j in brokenLetters:
                if j in word:
                    c += 1
                    break
        return len(words) - c

if __name__ == '__main__':
    # text = "hello world"
    # brokenLetters = "ad"
    text = "leet code"
    brokenLetters = "e"
    sol = Solution()
    print(sol.canBeTypedWords(text,brokenLetters))
