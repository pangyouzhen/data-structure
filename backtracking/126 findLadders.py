from typing import List
from collections import deque
from collections import defaultdict


#  最短路径，使用广度优先算法,所以首先构建个图
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        all_word = []
        all_word.append(beginWord)
        all_word.append(endWord)
        all_word.extend(wordList)
        # print(all_word)
        n_sim = len(list(beginWord))
        n = len(all_word)
        graph = defaultdict(list)

        def sim_word(s1, s2):
            t = 0
            m = 0
            while m < n_sim:
                if s1[m] != s2[m]:
                    t += 1
                if t > 1:
                    return False
                m += 1
            return True

        for i in range(n):
            for j in range(i):
                if sim_word(all_word[i], all_word[j]):
                    if all_word[j] not in graph[all_word[i]] and all_word[j] != all_word[i]:
                        graph[all_word[i]].append(all_word[j])
                    if all_word[i] not in graph[all_word[j]] and all_word[j] != all_word[i]:
                        graph[all_word[j]].append(all_word[i])
        # print(graph)
        return graph


if __name__ == '__main__':
    beginWord1 = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    sol = Solution()
    print(sol.findLadders(beginWord1, endWord, wordList))
