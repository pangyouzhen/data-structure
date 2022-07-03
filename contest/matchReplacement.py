from typing import List
import re
from collections import defaultdict

class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        # s = "fool3e7bar", sub = "leet", mappings = [["e","3"],["t","7"],["t","8"]]
        d = defaultdict(list)
        for i in mappings:
            d[i[0]].append(i[1])
        res = {}
        for i,v in d.items():
            res[i] = '[%s]'%(i + ''.join(v))
        sub_regex = []
        for i in sub:
            if i in res.keys():
                sub_regex.append(res[i])
            else:
                sub_regex.append(i)
        sub_regex = "".join(sub_regex)
        if re.search(sub_regex,s):
            return True
        return False
if __name__ == '__main__':
    func = Solution().matchReplacement
    s = "fool3e7bar"
    sub = "leet"
    mappings = [["e","3"],["t","7"],["t","8"]]
    print(func(s,sub,mappings))