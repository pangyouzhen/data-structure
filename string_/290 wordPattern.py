class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str_list = str.split()
        return [pattern.index(i) for i in pattern] == [str_list.index(i) for i in str_list]


if __name__ == '__main__':
    sol = Solution()
    assert sol.wordPattern("abba", "dog cat cat dog") == True
    assert sol.wordPattern("abba", "dog cat cat fish") == False
    assert sol.wordPattern("aaaa", "dog cat cat dog") == False
    assert sol.wordPattern("abba", "dog dog dog dog") == False
