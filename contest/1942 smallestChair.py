from typing import List


# TODO
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = list(zip(enumerate(times)))
        arrive_time = sorted(times, key=lambda x: x[1][0])
        for i,v in arrive_time:
            pass
        return times


if __name__ == '__main__':
    times = [[1, 4], [2, 3], [4, 6]]
    targetFriend = 1
    func = Solution().smallestChair
    print(func(times, targetFriend))
