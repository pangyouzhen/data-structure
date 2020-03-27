import string


class Solution:
    def isPalindrome(self, s):
        s_lower = s.lower().replace(" ", "")
        translator = str.maketrans("", "", string.punctuation)
        rm_punction = s_lower.translate(translator)
        left = 0
        right = len(rm_punction) - 1
        result = True
        while left < right:
            if rm_punction[left] != rm_punction[right]:
                result = False
                break
            else:
                left += 1
                right -= 1
        return result


if __name__ == '__main__':
    sol = Solution()
    assert sol.isPalindrome("race a car") ==  False
    assert sol.isPalindrome("A man, a plan, a canal: Panama") == True
