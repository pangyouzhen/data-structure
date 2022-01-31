from collections import Counter
from typing import List


class Solution():
    def uncommonFromSentences(self, s1: str, s2:str) -> List[str]:
        s = s1 +" " + s2
        s = s.split()
        print(s)
        c = Counter(s)
        return [i for i,v in c.items() if v == 1]
if __name__ =="__main__":
    func = Solution().uncommonFromSentences
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    print(func(s1,s2))
