def bubble_sort(alist):
    for i in range(1, len(alist)):
        for j in range(0, len(alist) - i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
            print(alist)


# 冒泡排序的主要思想是交换相邻的两个顺序
# 冒泡排序的时间复杂度是平均和最坏都是O(n^2)，最好的情况下是O(n)
if __name__ == '__main__':
    li = [5, 9, 3, 1, 2, 8, 4, 7, 6]
    bubble_sort(li)
    print("_________")
    print(li)
