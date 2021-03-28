from typing import List
import re


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        a_dict = {}
        for i in knowledge:
            a_dict[i[0]] = i[1]
        a = re.findall("\(\w+\)", s)
        if a:
            for t in a:
                w = t[1:-1]
                if w in a_dict.keys():
                    s = s.replace(t, a_dict[w])
                else:
                    s = s.replace(t, "?")
        return s


if __name__ == '__main__':
    s = "(name)is(age)yearsold"
    knowledge = [["name", "bob"], ["age", "two"]]
    sol = Solution()
    print(sol.evaluate(s, knowledge))
