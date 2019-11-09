from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        duplicate_ls = []
        for i, v in enumerate(strs):
            t = sorted(list(v))
            if t not in duplicate_ls:
                duplicate_ls.append(t)
                result.append([v])
            else:
                _ = duplicate_ls.index(t)
                result[_].append(v)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
