class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split(" ")
        if len(s) == 1:
            if s[0][-1] == s[0][0]:
                return True
        tail = s[0][-1]
        for i in range(1,len(s)):
            if s[i][0] == tail:
                tail = s[i][-1]
            else:
                return False
        return tail == s[0][0]
            