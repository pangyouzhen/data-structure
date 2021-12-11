from math import floor


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_b = text.count("b")
        count_a = text.count("a")
        count_l = floor(text.count("l") / 2)
        count_o = floor(text.count("o") / 2)
        count_n = text.count("n")
        return min([count_b, count_a, count_l, count_o, count_n])
