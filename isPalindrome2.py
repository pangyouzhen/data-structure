import string


class Solution:
    def isPalindrome(self, s):
        s_lower = s.lower().replace(" ", "")
        translator = str.maketrans("", "", string.punctuation)
        rm_punction = s_lower.translate(translator)
        if rm_punction[::-1] == rm_punction:
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    res = sol.isPalindrome("race a car")
    print(res)
