class Solution:
    def isAnagram(self, s, t):
        st = sorted(tuple(list(s)))
        tt = sorted(tuple(list(t)))
        if st == tt and len(s) == len(t):
            return True
        else:
            return False


if __name__ == '__main__':
    res = Solution().isAnagram
    assert res("anagram", "nagaram") == True
    assert res("rat", "car") == False
