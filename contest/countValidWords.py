import re

from pysnooper import snoop


class Solution:
    @snoop()
    # todo
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        res = 0
        for word in words:
            if re.search("\d", word):
                continue
            if re.match("^[a-z]+(-([a-z]+))?.?$", word):
                res += 1
                continue
            if re.match("^-$", word):
                continue
            if re.match("^.$", word):
                res += 1
                continue
        return res


if __name__ == '__main__':
    sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
    sentence2 = "!this  1-s b8d!"
    sentence3 = "cat and  dog"
    sentence4 = "alice and  bob are playing stone-game10"
    sentence5 = "-"
    sentence6 = "!"
    func = Solution().countValidWords
    assert func(sentence) == 6
    assert func(sentence2) == 0
    assert func(sentence3) == 3
    assert func(sentence4) == 5
    assert func(sentence5) == 0
    assert func(sentence6) == 1
