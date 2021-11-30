from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t = defaultdict(list)
        for i in strs:
            m = sorted(i)
            m_key = "".join(m)
            t[m_key].append(i)
        return list(t.values())


if __name__ == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
