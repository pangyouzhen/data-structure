class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        t = set(sentence)
        if len(t) != 26:
            return False
        return True


if __name__ == '__main__':
    sentence = "leetcode"
    sol = Solution()
    print(sol.checkIfPangram(sentence))
