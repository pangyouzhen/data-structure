from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if ransomNote:
            note_number = Counter(ransomNote)
            magazine_number = Counter(magazine)
            for i in note_number:
                if i not  in magazine_number or note_number[i] > magazine_number[i]:
                    return False
        return True

if __name__ == '__main__':
    sol = Solution()
    assert sol.canConstruct("a", "b") == False
    assert sol.canConstruct("aa", "ab") == False
    assert sol.canConstruct("aa", "aab") == True
    assert sol.canConstruct("fffbfg", "effjfggbffjdgbjjhhdegh") == True
    assert sol.canConstruct("bjaajgea",
                            "affhiiicabhbdchbidghccijjbfjfhjeddgggbajhidhjchiedhdibgeaecffbbbefiabjdhggihccec") == True
    assert sol.canConstruct("","") == True
    assert sol.canConstruct("","a") == True
    assert sol.canConstruct("fihjjjjei","hjibagacbhadfaefdjaeaebgi") == False