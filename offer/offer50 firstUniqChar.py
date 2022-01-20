import pysnooper


class Solution:
    # @pysnooper.snoop()
    def firstUniqChar(self, s: str) -> str:
        queue = []
        visited = []
        for i in s:
            if i not in queue and i not in visited:
                queue.append(i)
            else:
                visited.append(i)
                if i in queue:
                    queue.remove(i)
        if len(queue) > 0:
            return queue[0]
        else:
            return " "


if __name__ == '__main__':
    sol = Solution()
    print(sol.firstUniqChar("aadadaad"))
