# finished
# https://www.geeksforgeeks.org/merge-sort/
# https://visualgo.net/en/sorting
from typing import List

#  使用heaqp进行merge
from heapq import merge


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    # divide
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    #  merge
    return list(merge(left, right))


#  自定义merge
def merge_sort_(nums: List) -> List:
    if len(nums) < 2:
        return nums
    #  divide
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    #merge
    return merge_(left, right)


def merge_(left, right):
    res = []
    #  左右进行比较
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    #  当只有一个元素时添加进去
    res += left
    res += right
    return res


#  merge排序的时间复杂度是 nlog(n), 最坏情况下也是nlog(n)
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7, 78, 3]
    print("given array is ", end="\n")
    print("Sorted array is ", end="\n")
    print(merge_sort(arr))
    print(merge_sort_(arr))
