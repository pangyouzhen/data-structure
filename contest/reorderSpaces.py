import re


class Solution:
    def reorderSpaces(self, text: str) -> str:
        # 注意这里 直接用 text 就行
        words = [i for i in re.split('\s+', text) if i]
        space_nums = text.count(" ")
        n = len(words)
        if n - 1 == 0:
            return words[0] + space_nums * " "
        t = space_nums // (n - 1)
        res = ""
        for ind, word in enumerate(words):
            res += word
            if ind == len(words) - 1:
                res += space_nums * " "
            else:
                res += t * " "
            space_nums -= t

        return res


class Solution2:
    def reorderSpaces(self, text: str) -> str:
        cnt = text.count(" ")
        s = text.split()
        if len(s) == 1:
            return "".join(s) + " " * cnt
        d, m = divmod(cnt, len(s) - 1)
        return (" " * d).join(s) + " " * m


if __name__ == '__main__':
    func = Solution().reorderSpaces
    text = "  this   is  a sentence "
    print(func(text))
