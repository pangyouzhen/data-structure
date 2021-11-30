class Solution:
    # todo
    def removeDuplicateLetters(self, s: str) -> str:
        if len(s) == 1:
            return s
        queue = []
        for i in s:
            if i in s:
                ind = s.index(i)

            else:
                queue.append(s)
