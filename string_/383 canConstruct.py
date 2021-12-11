from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dic = Counter(ransomNote)
        magazine_dic = Counter(magazine)
        #  小字典 - 大字典
        condition = ransomNote_dic - magazine_dic
        if not condition:
            return True
        return False


if __name__ == '__main__':
    sol = Solution()
    assert sol.canConstruct("a", "b") == False
    assert sol.canConstruct("aa", "ab") == False
    assert sol.canConstruct("aa", "aab") == True
    assert sol.canConstruct("fffbfg", "effjfggbffjdgbjjhhdegh") == True
    assert sol.canConstruct("bjaajgea",
                            "affhiiicabhbdchbidghccijjbfjfhjeddgggbajhidhjchiedhdibgeaecffbbbefiabjdhggihccec") == True
    assert sol.canConstruct("", "") == True
    assert sol.canConstruct("", "a") == True
    assert sol.canConstruct("fihjjjjei", "hjibagacbhadfaefdjaeaebgi") == False
