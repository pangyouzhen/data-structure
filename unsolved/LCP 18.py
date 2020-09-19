from typing import List


class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        # 超时
        # staple.sort(reverse=True)
        # drinks.sort(reverse=True)
        # # print(f"{staple = },{drinks = }")
        # staple_index = 0
        # drinks_index = 0
        # res = 0
        # # result = []
        # while staple_index < len(staple):
        #     staple_val = staple[staple_index]
        #     if staple_val > x:
        #         staple_index += 1
        #         continue
        #     while drinks_index < len(drinks):
        #         loss = x - staple_val
        #         if drinks[drinks_index] > loss:
        #             drinks_index += 1
        #         else:
        #             res += len(drinks) - drinks_index
        #             # result.append((staple_index, drinks_index))
        #             break
        #     staple_index += 1
        #     drinks_index = 0
        #     # print(result)
        # return res % (10 ** 9 + 7)
        pass


if __name__ == '__main__':
    # staple = [10, 20, 5]
    # drinks = [5, 5, 2]
    # x = 15
    # staple = [6, 1, 9, 2, 9, 9, 3, 4]
    # drinks = [2, 7, 10, 2, 9, 2, 1, 3]
    # x = 2
    staple = [2, 1, 1]
    drinks = [8, 9, 5, 1]
    x = 9
    sol = Solution()
    print(sol.breakfastNumber(staple, drinks, x))
