def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        min_value = min(alist[i:])
        min_index = alist.index(min_value)
        alist[i], alist[min_index] = min_value, alist[i]
        print(alist)


# 选择排序的主要思想是 ，缩小list范围，选出最小的进行交换
if __name__ == "__main__":
    arr = [6, 1, 7, 8, 9, 3, 5, 4, 2]
    selection_sort(arr)
    print('----------------')
    print(arr)
