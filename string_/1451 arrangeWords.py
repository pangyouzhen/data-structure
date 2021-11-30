class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower()
        text_split = text.split(" ")
        sort_text = sorted(text_split, key=len)
        sort_text[0] = sort_text[0].capitalize()
        return " ".join(sort_text)


if __name__ == '__main__':
    text = "To be or not to be"
    text2 = "Keep calm and code on"
    sol = Solution()
    print(sol.arrangeWords(text))
    print(sol.arrangeWords(text2))
